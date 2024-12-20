# ----------------------------------------------------------------------------------------------------------
# $GUI v1.0
# Author: David Francois
# Copyright (c) 2024, David Francois
# ----------------------------------------------------------------------------------------------------------

import nuke

# Disable or enable nodes based on their current state
def run_all():
    # Iterate through all nodes in the scene
    for node in nuke.allNodes():
        # Check if the node name contains specific keywords
        if any(x in node.name() for x in ["Defocus", "VectorBlur", "Denoise"]):
            disable_knob = node['disable']

            # Manage expressions or animations on the "disable" knob
            if disable_knob.isAnimated():
                disable_knob.clearAnimated()  # Remove all animations/expressions
                disable_knob.setValue(0)  # Disable the node
                print(f"Animation cleared and {node.name()} disabled.")
            else:
                disable_knob.setExpression("$gui")  # Add the "$gui" expression
                disable_knob.setValue(1)  # Enable the node
                print(f"Expression $gui added and {node.name()} enabled.")

# Manage the selected nodes in the scene
def run():
    selected_nodes = nuke.selectedNodes()
    if not selected_nodes:
        nuke.message("No nodes selected.")
        return

    for node in selected_nodes:
        try:
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
        except KeyError:
            nuke.message(f"The node {node.name()} does not have a 'disable' knob.")
            continue
