#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# fichier: par-ici-la-sortie.py
#  auteur: Julien FORTINEAU
#    date: 2026-7-1

import modules

evenements = modules.Charger()
recherche = modules.Recherche(evenements)


def TuiPils():
    """Lance le TUI de pils"""
    run = True
    print(" Bienvenue sur l'interface terminal de Par ici la sortie!")
    while run:
        run = SelectionneAction()


def SelectionneAction():
    print()
    print(" Que voulez vous faire ?")
    r = input(
""" 1- Voir les événements    2- Ajouter un événement    3- Modifier un événement    4- Sauvegarder
 5- MAJ les fichiers guides    6- Quitter & Sauvegarder    7- Quitter sans sauvegarder
""")

    if r == '1':
        run = True
        while run:
            run = AfficherEvents(evenements, True)
    elif r == '2':
        AjouterEvenements()
    elif r == '3':
        run = True
        while run:
            run = ModifierEvenement()
    elif r == '4':
        Sauvegarder()
    elif r == '5':
        MajGuides()
    elif r == '6':
        Sauvegarder()
        return False
    elif r == '7':
        return False
    else:
        print(" Requête non comprise.")
    return True


def AfficherEvents(events, options:bool):
    print()
    if len(events) == 0:
        print("Aucun événements trouvés")
    for id, event in events.items():
        print (f" Événement {id}: {event}")
    if options:
        print(" Que voulez vous faire ?")
        r = input(
            """ 1- Chercher un événements    2- Retour
""")
        if r == '1':
            Recherche()
        elif r == '2':
            return False
        else:
            print("Requête non comprise.")
        return True


def AjouterEvenements():
    print()
    v = False
    nom = input("Quel est le nom de l'événement ? : ")
    lieu = input("Où se déroule l'événement ? : ")
    date = None
    while not v:
        j = input("Quel jour se déroule l'événement ? (entre 1 et 31) : ")
        m = input("Quel mois se déroule l'événement ? (entre 1 et 12) : ")
        a = input("Quel année se déroule l'événement ? : ")
        try:
            date = modules.Date(j, m, a)
            date.est_passee()
        except Exception:
            print("La date n'est pas valide, veuillez réessayer :")
        else:
            v = True
    contact = input("Quel contact les client devrais avoir ? : ")
    v = False
    prix = None
    while not v:
        try:
            prix = bool(int(input("Quel est le prix de l'événement ? (0 gratuit, 1 payant) : ")))
        except Exception:
            print("Le prix n'est pas valide, veuillez réessayer :")
        else:
            v = True
    modules.CreerEvenement(evenements, nom, lieu, date, contact, prix)


def ModifierEvenement():
    print()
    id = input("Quel est l'ID de l'événement que vous voulez modifier ? (tapez R pour rechercher, Q pour quitter) : ")

    if id.lower() == "r":
        Recherche()

    elif id.lower() == "q":
        return False

    elif id.isnumeric() and 0 <= int(id) <= len(evenements):
        id = int(id)

        nom = input("Voulez vous modifier le nom de l'événement ? (o ou n) : ")
        if nom.lower() == "o":
            nom = input("Quel est le nouveau nom ? : ")
        else:
            nom = None

        lieu = input("Voulez vous modifier le lieu de l'événement ? (o ou n) : ")
        if lieu.lower() == "o":
            lieu = input("Quel est le nouveau lieu ? : ")
        else:
            lieu = None

        v = False
        date = input("Voulez vous modifier la date de l'événement ? (o ou n) : ")
        if date.lower() == "o":
            while not v:
                j = input("Quel jour se déroule l'événement ? (entre 1 et 31) : ")
                m = input("Quel mois se déroule l'événement ? (entre 1 et 12) : ")
                a = input("Quel année se déroule l'événement ? : ")
                try:
                    date = modules.Date(j, m, a)
                    date.est_passee()
                except Exception:
                    print("La date n'est pas valide, veuillez réessayer : ")
                else:
                    v = True
        else:
            date = None

        contact = input("Voulez vous modifier le contact de l'événement ? (o ou n) : ")
        if contact.lower() == "o":
            contact = input("Quel est le nouveau contact ? : ")
        else:
            contact = None

        v = False
        prix = input("Voulez vous modifier le prix de l'événement ? (o ou n) :")
        if prix.lower() == "o":
            while not v:
                try:
                    prix = int(input("Quel est le prix de l'événement ? (0 gratuit, 1 payant) : "))
                    if prix ==0:
                        prix = True
                    else:
                        prix = False
                except Exception:
                    print("Le prix n'est pas valide, veuillez réessayer : ")
                else:
                    v = True
        else:
            prix = None

        modules.ModifierEvenement(evenements, id, nom, lieu, date, contact, prix)

    else:
        print("L'ID n'est pas valide.")

    return True


def Sauvegarder():
    print()
    try:
        modules.Sauver(evenements)
    except Exception as e:
        print(f"Erreur lors de la sauvegarde: {e}")
    else:
        print("sauvegardé avec succès")


def MajGuides():
    print()
    try:
        modules.GenererHtml()  # Ajouter le code du PDF si fini par Louis
    except Exception as e:
        print(f"Erreur lors de la mise à jour de guide.html: {e}")
        raise e
    else:
        print("Mis à jour avec succès")


def Recherche():
    print()
    run = True
    while run:
        r = input('Recherche (/q pour quitter) : ')
        if r == "/q":
            run = False
        else:
            result = recherche.Recherche(r)
            AfficherEvents(result, False)


TuiPils()
