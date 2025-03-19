
## $GUI Toggle

`$GUI` is a Nuke tool designed to manage the disable knob and optimize workflows.

The `$gui` expression is a simple TCL command in Nuke that temporarily disables heavy nodes when viewing in the Viewer while keeping them active during farm rendering. This expression can improve workflow speed in complex Nuke scripts. By applying `$gui` to resource-intensive nodes, they are ignored in the Viewer display, providing a simplified and faster proxy version. However, during the final render on the farm, these nodes are reactivated, ensuring optimal quality.

### Features

- **$GUI (Shortcut: Alt+D):** Adds the `$gui` expression to the selected node's disable knob.
- **$GUI All (Shortcut: Alt+4):** Ensures specified nodes are dynamically disabled in GUI mode and enabled during rendering.
- **$GUI Settings (Shortcut: Shift+Alt+D):** Configure which nodes are affected by the script.


![gui_demo](https://github.com/user-attachments/assets/49d1194d-f4d2-4ff6-bdff-054c68465831)

### Configuration

In version 1.2, you can specify how nodes are targeted by `$GUI`:

- **Filter by Name:** Nodes are identified based on their names. For example, nodes containing "defocus", "vector", or "denoise" in their names.
- **Filter by Class:** Nodes are identified based on their class type, such as `Defocus`, `VectorBlur`, or `Denoise`.

To configure:

1. Open the `$GUI Settings` panel (Shortcut: Shift+Alt+D).
2. Choose whether to filter nodes by their name or class.
3. Enter the list of node identifiers (separated by commas) that you want `$GUI` to affect.

### Installation

1. Place the `gui.py` and `gui_settings.json` files in the `.nuke` directory:

   - **Windows:** `%HOME%/.nuke/`
   - **macOS/Linux:** `~/.nuke/`

2. Add the following commands to your `menu.py` file located in the same `.nuke` directory:

   ```python
   import nuke
   import gui

   # Add a custom menu in Nuke
   dd_tools_menu = nuke.menu('Nuke').addMenu('DD Tools')
   dd_tools_menu.addCommand('$gui', 'gui.run()', 'Alt+D')
   dd_tools_menu.addCommand('$gui all', 'gui.run_all()', 'Alt+4')
   dd_tools_menu.addCommand('$gui setting', 'gui.setting()', 'Shift+Alt+D')
   ```

   This script creates a new menu titled "DD Tools" in Nuke's menu bar, providing quick access to the `$GUI` functionalities with assigned shortcuts.
