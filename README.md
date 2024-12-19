## $GUI Toggle

**$GUI Toggle** is a Nuke script that automates the management of the **disable** knob for specific nodes, such as `Defocus`, `VectorBlur`, and `Denoise`.

### Features

- **Single Node Management**: Apply or remove the `$gui` expression on the `disable` knob of selected nodes.
- **Global Application**: Automatically apply `$gui` to all relevant nodes in the scene (e.g., `Defocus`, `VectorBlur`, `Denoise`).
- **Expression Control**: Ensures nodes are dynamically disabled in GUI mode and enabled during rendering.


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
