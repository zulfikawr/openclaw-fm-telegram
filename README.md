# openclaw-fm-telegram

a telegram-based file manager for openclaw using inline buttons and local file navigation.

## 🚀 features

- **native navigation**: browse directories using telegram inline buttons.
- **file uploads**: click any file to have it uploaded directly to your telegram chat.
- **secure**: path-prefix restricted to ensure you stay within allowed directories.
- **lightweight**: simple python script with no heavy dependencies.

## 🛠️ how to use

1. **initialization**:
   run the script with the `fm` argument to start the file manager at the root.
   ```bash
   python3 file_manager.py fm
   ```

2. **navigation**:
   - click **📁 [directory]** to enter a folder.
   - click **⬅️ Back** to go up one level.

3. **file access**:
   - click **📄 [filename]** to have the file uploaded to the chat.

## ⚙️ integration with openclaw

to use this as a custom command (e.g., `/fm`), you can integrate it into your openclaw gateway configuration.

### script location
place `file_manager.py` in your openclaw workspace.

### state management
the script maintains navigation state in `fm_state.json` to track your current path and history.
