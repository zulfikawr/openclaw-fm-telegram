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

to use this as a custom command (e.g., `/fm`) without losing your default openclaw commands, follow these steps:

### 1. script location
place `file_manager.py` in your openclaw workspace.

### 2. update openclaw configuration
**do not manually set commands in botfather.** instead, use the openclaw config to register custom commands. this ensures that the native openclaw commands are preserved alongside the file manager.

edit your `~/.openclaw/openclaw.json` (or use the `gateway` tool if you are an agent) to include the following in the `channels.telegram` section:

```json
{
  "channels": {
    "telegram": {
      "customCommands": [
        {
          "command": "fm",
          "description": "open telegram file manager"
        }
      ]
    }
  }
}
```

### 3. restart the gateway
after updating the config, restart your openclaw gateway. it will automatically sync the new command list with telegram while keeping the defaults:

```bash
openclaw gateway restart --force
```

### ⚠️ warning
using `@BotFather` to set commands will **overwrite** the entire menu list, hiding openclaw's native commands. always use the `customCommands` config option in openclaw instead.

## 💾 state management
the script maintains navigation state in `fm_state.json` to track your current path and history.
