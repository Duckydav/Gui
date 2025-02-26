import nuke
import gui

# Add a custom menu in Nuke
dd_tools_menu = nuke.menu('Nuke').addMenu('DD Tools')
dd_tools_menu.addCommand('$gui', 'gui.run()', 'Alt+D')
dd_tools_menu.addCommand('$gui all', 'gui.run_all()', 'Alt+4')
dd_tools_menu.addCommand('$gui setting', 'gui.setting()', 'Shift+Alt+D')
