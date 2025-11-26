""" ce programe permet de modifier des evenements"""

modifier_evenement(index, nouvel_evenement):
    """Remplace un événement existant par un nouveau."""
    index -= 1
    if 0 <= index < len(liste_evenements):
        liste_evenements[index] = nouvel_evenement
        print("Événement modifié avec succès !")
    else:
        print("Index invalide, impossible de modifier.")
