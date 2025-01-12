# ----------------------------------------------------------------------------------------------------------
# $GUI v1.1
# Author: David Francois
# Copyright (c) 2024, David Francois
# ----------------------------------------------------------------------------------------------------------

import nuke
import json
import os

# Path to the JSON settings file
SETTINGS_PATH = os.path.expanduser("~/.nuke/gui_settings.json")


def load_settings():
    # If the JSON file doesn't exist, create it with default values
    if not os.path.exists(SETTINGS_PATH):
        initial_settings = {"node_names": ["defocus", "vector", "denoise"]}  # Default values
        save_settings(initial_settings)
        return initial_settings
    # Load settings from the JSON file
    with open(SETTINGS_PATH, 'r') as file:
        return json.load(file)


def save_settings(settings):
    # Save the settings to the JSON file
    with open(SETTINGS_PATH, 'w') as file:
        json.dump(settings, file, indent=4)


def setting():
    # Load current settings
    settings = load_settings()
    node_names = settings.get("node_names", [])

    # Configuration window
    input_label = "<h2>Node's names</h2>\n\nto be affected by\n$gui in Disable\n\n(list separated by commas)"
    panel = nuke.Panel("$GUI Settings")
    panel.addNotepad(input_label, ", ".join(node_names))

    if panel.show():
        # Update node names from user input
        new_names = panel.value(input_label).strip().split(',')
        settings["node_names"] = [name.strip().lower() for name in new_names if name.strip()]
        save_settings(settings)


# Disable or enable nodes based on their current state
def run_all():
    # Load settings and get node names
    settings = load_settings()
    node_names = [name.lower() for name in settings.get("node_names", [])]

    for node in nuke.allNodes():
        # Check if the node name matches any in the list
        if any(x in node.name().lower() for x in node_names):
            disable_knob = node['disable']

            if disable_knob.isAnimated():
                # Clear animation and disable the node
                disable_knob.clearAnimated()
                disable_knob.setValue(0)
                print(f"Animation cleared and {node.name()} disabled.")
            else:
                # Add $gui expression and enable the node
                disable_knob.setExpression("$gui")
                disable_knob.setValue(1)
                print(f"Expression $gui added and {node.name()} enabled.")


# Manage the selected nodes in the scene
def run():
    # Get selected nodes
    selected_nodes = nuke.selectedNodes()
    if not selected_nodes:
        nuke.message("No nodes selected.")
        return

    for node in selected_nodes:
        disable_knob = node['disable']
        current_expression = disable_knob.toScript().strip()  # Get the current expression

        if "$gui" in current_expression:
            # Remove the $gui expression and reset
            disable_knob.setExpression("")
            disable_knob.clearAnimated()
            disable_knob.setValue(0)
            print(f"Expression '$gui' removed for {node.name()}.")
        else:
            # Add the $gui expression
            disable_knob.clearAnimated()
            disable_knob.setExpression("$gui")
            print(f"Expression '$gui' added to {node.name()}.")
