""" ce programe permet de modifier des evenements"""

import evenement as e

def modifier_evenement(liste_event, index, nom=None, place=None, date=None, contact=None, prix=None):
    """Remplace un événement existant par un nouveau."""
    if 0 <= index < len(liste_event):
        event = liste_event[str(index)]
        if nom is not None: event.nom = nom
        if place is not None: event.place = place
        if date is not None: event.date = date
        if contact is not None: event.contact = contact
        if prix is not None: event.prix = prix

        print("Événement modifié avec succès !")
    else:
        print("Index invalide, impossible de modifier.")


if __name__ == '__main__':

    import GererLaData as g

    l = g.Charger()

    modifier_evenement(l, 2, nom='Le merveilleux Noël')

    print(l['2'])

    g.Sauver