from tkinter import *

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
    text="Bienvenue sur l'application",
    font=("Courrier", 40),
    bg="#41B77F",
    fg="white"
)
label_title.pack(pady=20)

# Fonction pour ajouter un événement (à compléter)
def ajouter_evenement():
    print("Ajouter un événement")

# Fonction pour modifier un événement (à compléter)
def modifier_evenement():
    print("Modifier mes événements")

# Bouton "Ajouter un événement"
bouton_ajouter = Button(
    window,
    text="Ajouter un événement",
    font=("Courrier", 16),
    bg="white",
    fg="#41B77F",
    command=ajouter_evenement
)
bouton_ajouter.pack(pady=10)

# Bouton "Modifier mes événements"
bouton_modifier = Button(
    window,
    text="Modifier mes événements",
    font=("Courrier", 16),
    bg="white",
    fg="#41B77F",
    command=modifier_evenement
)
bouton_modifier.pack(pady=10)

# Afficher
window.mainloop()
