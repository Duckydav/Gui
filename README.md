## $GUI Toggle

**$gui** is a tool for Nuke designed to manage the disable knob and optimize workflows.

The `$gui` expression is a simple TCL command in Nuke that temporarily disables heavy nodes when viewing in the Viewer while keeping them active during farm rendering.  
This expression can be used to improve workflow speed in complex Nuke scripts. By applying `$gui` to resource-intensive nodes, they are ignored in the Viewer display, providing a simplified and faster proxy version. However, during the final render on the farm, these nodes are reactivated, ensuring optimal quality.

### Features

- **$Gui (Shortcut: Alt+D)**: On the selected node - Adds the `$gui` expression to the node's disable knob.
- **$gui all (Shortcut: Alt+4)**: Multiple Nodes - Ensures nodes are dynamically disabled in GUI mode and enabled during rendering.

### Notes

At line 14 of `gui.py`, you have the option to add or modify the names of the nodes you want the function to include.  
Currently, it targets nodes with the names `Defocus`, `VectorBlur`, and `Denoise`.

![gui_demo](https://github.com/user-attachments/assets/49d1194d-f4d2-4ff6-bdff-054c68465831)

## ***Installation***

1. Place the `gui.py` file in the **`.nuke`** directory:
   - **Windows**: `%HOME%/.nuke/`
   - **macOS/Linux**: `~/.nuke/`

2. Add the following command to your `menu.py` file located in the same `.nuke` directory:

   ```python
   import nuke
   import gui

   # Add a custom menu in Nuke
   dd_tools_menu = nuke.menu('Nuke').addMenu('DD Tools')
   dd_tools_menu.addCommand('$gui', 'gui.run()', 'Alt+D')
   dd_tools_menu.addCommand('$gui all', 'gui.run_all()', 'Alt+4')
