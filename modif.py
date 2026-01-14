from tkinter import *

class MyWindow(Tk):
    def __init__(self):
        Tk.__init__(self)
        # Variables pour stocker les informations
        self.__name = StringVar()
        self.__date = StringVar()
        self.__location = StringVar()
        self.__contact = StringVar()
        self.__is_free = StringVar(value="gratuit")  # Par défaut : gratuit

        # Titre de la fenêtre
        self.title("Modifier un évènement")
        self.geometry("400x400")

        # Champ Nom
        Label(self, text="Nom  :").pack(pady=5)
        Entry(self, textvariable=self.__name).pack(pady=5)
        # Champ Date
        Label(self, text="Date (AAAA/MM/JJ) :").pack(pady=5)
        Entry(self, textvariable=self.__date).pack(pady=5)
        # Champ Localisation
        Label(self, text="Localisation :").pack(pady=5)
        Entry(self, textvariable=self.__location).pack(pady=5)
        # Champ Contact
        Label(self, text="Contact (email/téléphone/URL) :").pack(pady=5)
        Entry(self, textvariable=self.__contact).pack(pady=5)

        # Choix Gratuit/Payant (boutons radio)
        Label(self, text="Type d'événement :").pack(pady=5)
        Radiobutton(self, text="Gratuit", variable=self.__is_free, value="gratuit").pack()
        Radiobutton(self, text="Payant", variable=self.__is_free, value="payant").pack()

        # Bouton Valider
        Button(self, text="Exporter", command=self.validate).pack(pady=10)

    def validate(self):
        # Afficher les informations saisies
        print("Nom :", self.__name.get())
        print("Date :", self.__date.get())
        print("Localisation :", self.__location.get())
        print("Contact :", self.__contact.get())
        print("Type :", self.__is_free.get())

# Instanciation et lancement
window = MyWindow()
window.mainloop()
