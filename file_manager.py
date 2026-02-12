#!/usr/bin/env python3

import sys
import os
import json

workspace = "/home/zulfikar"
state_file = "/home/zulfikar/.openclaw/workspace/fm_state.json"

def load_state():
    if os.path.exists(state_file):
        with open(state_file) as f:
            return json.load(f)
    return {"current_path": workspace, "path_history": [workspace]}

def save_state(state):
    with open(state_file, 'w') as f:
        json.dump(state, f)

def is_safe_path(path):
    if not path.startswith(workspace):
        return False
    rel_path = os.path.relpath(path, workspace)
    if rel_path == '.':
        return True
    depth = rel_path.count(os.sep)
    return depth <= 5

def list_directory(path):
    if not is_safe_path(path):
        return [], []
    try:
        # Include hidden files
        items = os.listdir(path)
        dirs = sorted([i for i in items if os.path.isdir(os.path.join(path, i))])
        files = sorted([i for i in items if os.path.isfile(os.path.join(path, i))])
        return dirs, files
    except:
        return [], []

def view_file(path, name):
    full_path = os.path.join(path, name)
    if not os.path.isfile(full_path) or not is_safe_path(full_path):
        return "File not found"
    try:
        with open(full_path, 'r') as f:
            content = f.read(2000)
        return content
    except Exception as e:
        return f"Error: {e}"

def send_listing(state):
    path = state['current_path']
    dirs, files = list_directory(path)
    
    # Simplified header
    msg = f"📂 `{path}`"
    
    # Buttons part
    buttons = []
    
    # Back button row
    if len(state['path_history']) > 1:
        buttons.append([{"text": "⬅️ Back", "callback_data": "back"}])
    
    # Directories
    for d in dirs:
        buttons.append([{"text": f"📁 {d}", "callback_data": f"enter:{d}"}])
        
    # Files
    for f in files:
        buttons.append([{"text": f"📄 {f}", "callback_data": f"view:{f}"}])

    print("SEND_MESSAGE:", msg)
    print("INLINE_KEYBOARD:", buttons)

def handle_callback(callback_data, state):
    updated = False
    if callback_data.startswith("enter:"):
        dir_name = callback_data[6:]
        new_path = os.path.join(state['current_path'], dir_name)
        if is_safe_path(new_path) and os.path.isdir(new_path):
            state['path_history'].append(state['current_path'])
            state['current_path'] = new_path
            updated = True
    elif callback_data.startswith("view:"):
        file_name = callback_data[5:]
        full_path = os.path.join(state['current_path'], file_name)
        if os.path.isfile(full_path) and is_safe_path(full_path):
            print("UPLOAD_FILE:", full_path)
        else:
            print("SEND_MESSAGE: File not found")
    elif callback_data == "back":
        if len(state['path_history']) > 1:
            state['current_path'] = state['path_history'].pop()
            updated = True
    if updated:
        save_state(state)
        send_listing(state)

def handle_fm():
    state = {"current_path": workspace, "path_history": [workspace]}
    save_state(state)
    send_listing(state)

if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1] == "fm":
        handle_fm()
    elif len(sys.argv) == 3 and sys.argv[1] == "callback":
        state = load_state()
        handle_callback(sys.argv[2], state)
    else:
        print("Usage: python3 file_manager.py fm | callback <data>")