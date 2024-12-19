# ----------------------------------------------------------------------------------------------------------
# $GUI v1.0
# Author: David Francois
# Copyright (c) 2024, David Francois




# ----------------------------------------------------------------------------------------------------------
# modules
# ----------------------------------------------------------------------------------------------------------

import nuke

def run_all():
    # Parcourir tous les nœuds dans la scène
    for node in nuke.allNodes():
        # Vérifier si le nom du nœud contient "Defocus"
        if "Defocus" in node.name() or "VectorBlur" in node.name() or "Denoise" in node.name():
            # Accéder au knob "disable"
            disable_knob = node['disable']

            # Vérifier si le knob "disable" a une animation (expression) attachée
            if disable_knob.isAnimated():
                # Si le knob est animé, on supprime l'animation (efface l'expression)
                disable_knob.clearAnimated()  # Supprimer toute animation/expression
                disable_knob.setValue(0)  # Désactiver le nœud
                print(f"Expression effacée et {node.name()} désactivé.")
            else:
                # Sinon, ajouter l'expression "$gui" et activer le nœud
                disable_knob.setExpression("$gui")
                disable_knob.setValue(1)  # Activer le nœud
                print(f"Expression $gui ajoutée et {node.name()} activé.")

def run():
    # Vérifie si des nœuds sont sélectionnés
    selected_nodes = nuke.selectedNodes()
    if not selected_nodes:
        nuke.message("Aucun nœud sélectionné.")
        return

    for node in selected_nodes:
        try:
            # Récupère la valeur actuelle ou l'expression du champ disable
            current_expression = node['disable'].toScript().strip()  # Supprime les espaces inutiles
            print(f"{node.name()} - État actuel du 'disable': '{current_expression}'")
        except KeyError:
            nuke.message(f"Le nœud {node.name()} n'a pas de champ 'disable'.")
            continue

        if "$gui" in current_expression:
            # Si l'expression contient $gui, on la supprime et réinitialise la valeur
            node['disable'].setExpression("")  # Supprime toute expression
            node['disable'].clearAnimated()   # Supprime toute animation
            node['disable'].setValue(False)   # Réinitialise à la valeur par défaut sans clé
            print(f"Expression '$gui' supprimée et remise à défaut pour {node.name()}")
        else:
            # Sinon, supprime toute animation existante, puis ajoute l'expression $gui
            node['disable'].clearAnimated()   # Assure qu'il n'y a pas de clés d'animation
            node['disable'].setValue(False)   # Réinitialise d'abord à False
            node['disable'].setExpression("$gui")  # Ajoute l'expression sans créer de clé
            print(f"Expression '$gui' ajoutée à {node.name()}")

