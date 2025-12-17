from tkinter import *

class MyWindow(Tk):
    def __init__(self):
        Tk.__init__(self)

        # Variables pour stocker les informations
        self.__name = StringVar()
        self.__date = StringVar()
        self.__location = StringVar()
        self.__contact = StringVar()

        # Nouvelle variable pour le menu déroulant
        self.__status = StringVar()
        self.__status.set("À venir")  # valeur par défaut

        # Titre de la fenêtre
        self.title("Informations sur l'événement")
        self.geometry("400x300")

        # Champ Nom
        Label(self, text="Nom :").pack(pady=5)
        Entry(self, textvariable=self.__name).pack(pady=5)

        # Champ Date et menu déroulant
        Label(self, text="Date (AAAA/MM/JJ) :").pack(pady=5)

        frame_date = Frame(self)
        frame_date.pack(pady=5)

        Entry(frame_date, textvariable=self.__date, width=20).pack(side=LEFT)

        OptionMenu(frame_date, self.__status, "À venir", "En cours").pack(side=LEFT, padx=10)

        # Champ Localisation
        Label(self, text="Localisation :").pack(pady=5)
        Entry(self, textvariable=self.__location).pack(pady=5)

        # Champ Contact
        Label(self, text="Contact (email/téléphone/URL) :").pack(pady=5)
        Entry(self, textvariable=self.__contact).pack(pady=5)

        # Bouton pour valider
        button = Button(self, text="SUIVANT", command=self.doSomething)
        button.pack()

    def doSomething(self):
        # Afficher les informations saisies
        print("Nom :", self.__name.get())
        print("Date :", self.__date.get())
        print("Statut :", self.__status.get())
        print("Localisation :", self.__location.get())
        print("Contact :", self.__contact.get())


window = MyWindow()
window.mainloop()
