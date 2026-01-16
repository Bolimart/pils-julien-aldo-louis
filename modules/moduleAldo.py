from tkinter import *
import modules

class FenetreAjouter(Tk):

    def __init__(self, retourne):
        Tk.__init__(self)
        #Délégué de la fonction retourne
        self.retourne = retourne

        # Variables pour stocker les informations
        self.__nom = StringVar()
        self.__date = StringVar()
        self.__localisation = StringVar()
        self.__contact = StringVar()
        self.__estGratuit = BooleanVar(value=False)  # Par défaut : gratuit

        # Titre de la fenêtre
        self.title("Ajouter un évènement")
        self.geometry("400x400")

        # Champ Nom
        Label(self, text="Nom  :").pack(pady=5)
        Entry(self, textvariable=self.__nom).pack(pady=5)
        # Champ Date
        Label(self, text="Date (AAAA/MM/JJ) :").pack(pady=5)
        Entry(self, textvariable=self.__date).pack(pady=5)
        # Champ Localisation
        Label(self, text="Localisation :").pack(pady=5)
        Entry(self, textvariable=self.__localisation).pack(pady=5)
        # Champ Contact
        Label(self, text="Contact (email/téléphone/URL) :").pack(pady=5)
        Entry(self, textvariable=self.__contact).pack(pady=5)

        # Choix Gratuit/Payant (boutons radio)
        Label(self, text="Type d'événement :").pack(pady=5)
        Radiobutton(self, text="Gratuit", variable=self.__est_gratuit, value=True).pack()
        Radiobutton(self, text="Payant", variable=self.__est_gratuit, value=False).pack()

        # Bouton Valider
        Button(self, text="Exporter", command=self.validate).pack(pady=10)


    def validate(self):
        # Afficher les informations saisies
        print("Nom :", self.__nom.get())
        print("Date :", self.__date.get())
        print("Localisation :", self.__localisation.get())
        print("Contact :", self.__contact.get())
        print("Type :", self.__est_gratuit.get())

        # Créer l'évènement
        d = self.__date.get().split('-')
        date = modules.Date(d[1], d[2], d[0])
        self.retourne(self.__nom.get(), self.__localisation.get(), date, self.__contact.get(), self.__est_gratuit.get())



class FenetreModifier(Tk):

    def __init__(self, retourne, id):
        Tk.__init__(self)
        #Délégué de la fonction retourne
        self.retourne = retourne

        # Variables pour stocker les informations
        self.id = id
        self.__nom = StringVar()
        self.__date = StringVar()
        self.__localisation = StringVar()
        self.__contact = StringVar()
        self.__est_gratuit = BooleanVar(value=True)  # Par défaut : payant

        # Titre de la fenêtre
        self.title("Modifier un évènement")
        self.geometry("400x400")

        # Champ Nom
        Label(self, text="Nom  :").pack(pady=5)
        Entry(self, textvariable=self.__nom).pack(pady=5)
        # Champ Date
        Label(self, text="Date (AAAA/MM/JJ) :").pack(pady=5)
        Entry(self, textvariable=self.__date).pack(pady=5)
        # Champ Localisation
        Label(self, text="Localisation :").pack(pady=5)
        Entry(self, textvariable=self.__localisation).pack(pady=5)
        # Champ Contact
        Label(self, text="Contact (email/téléphone/URL) :").pack(pady=5)
        Entry(self, textvariable=self.__contact).pack(pady=5)

        # Choix Gratuit/Payant (boutons radio)
        Label(self, text="Type d'événement :").pack(pady=5)
        Radiobutton(self, text="Gratuit", variable=self.__est_gratuit, value=True).pack()
        Radiobutton(self, text="Payant", variable=self.__est_gratuit, value=False).pack()

        # Bouton Valider
        Button(self, text="Exporter", command=self.validate).pack(pady=10)


    def validate(self):
        # Afficher les informations saisies
        print("Nom :", self.__nom.get())
        print("Date :", self.__date.get())
        print("Localisation :", self.__localisation.get())
        print("Contact :", self.__contact.get())
        print("Type :", self.__est_gratuit.get())

        # Crée l'évènement
        d = self.__date.get().split('/')
        date = modules.Date(d[1], d[2], d[0])
        self.retourne(self.id, self.__nom.get(), self.__localisation.get(), date, self.__contact.get(), self.__est_gratuit.get())


class FenetrePrincipale:

    def __init__(self, fenetreAjouter, fenetreModifier, fenetreAfficher, sauver, exporter):
        # Créer une première fenêtre
        window = Tk()
        # Personnaliser cette fenêtre
        window.title("My Application")
        window.geometry("1080x720")
        window.minsize(480, 360)
        window.config(background="#41B77F")

        # Ajouter un premier texte
        label_title = Label(
            window,
            text="Bienvenue sur Par ici la sortie!",
            font=("Courrier", 40),
            bg="#41B77F",
            fg="white"
        )
        label_title.pack(pady=20)

        # Bouton "Afficher les événements"
        bouton_ajouter = Button(
            window,
            text="Afficher les événements",
            font=("Courrier", 16),
            bg="white",
            fg="#41B77F",
            command=fenetreAfficher
        )
        bouton_ajouter.pack(pady=10)

        # Bouton "Ajouter un événement"
        bouton_ajouter = Button(
            window,
            text="Ajouter un événement",
            font=("Courrier", 16),
            bg="white",
            fg="#41B77F",
            command=fenetreAjouter
        )
        bouton_ajouter.pack(pady=10)

        # Bouton "Modifier mes événements"
        bouton_modifier = Button(
            window,
            text="Modifier mes événements",
            font=("Courrier", 16),
            bg="white",
            fg="#41B77F",
            command=fenetreModifier
        )
        bouton_modifier.pack(pady=10)

        # Bouton "Sauvegarder"
        bouton_modifier = Button(
            window,
            text="Sauvegarder",
            font=("Courrier", 16),
            bg="white",
            fg="#41B77F",
            command=sauver
        )
        bouton_modifier.pack(pady=10)

        # Bouton "Exporter les fichiers guides"
        bouton_modifier = Button(
            window,
            text="Exporter les fichiers guides",
            font=("Courrier", 16),
            bg="white",
            fg="#41B77F",
            command=exporter
        )
        bouton_modifier.pack(pady=10)

        # Bouton "Quitter"
        bouton_modifier = Button(
            window,
            text="Quitter",
            font=("Courrier", 16),
            bg="white",
            fg="#41B77F",
            command=lambda: window.destroy()
        )
        bouton_modifier.pack(pady=10)

        window.mainloop()
