#!/usr/bin/python3

from tkinter import Tk, Button, Label


# On définit un gestionnaire d'événements pour le bouton payant.
def do_something():
    print("payant")
    
# On definit un gestionnaire d'évenements pour le bouton gratuit.

def do_another_thing():
    print("gratuit")
# On instancie notre fenêtre graphique
window = Tk()

# On injecte un premier label dans la fenêtre
button = Button(window, text="Gratuit", command=do_another_thing)
button.pack()

# Puis, on injecte un bouton dans la fenêtre. Il est connecté à la
# fonction do_something qui déclenchera au clic sur le bouton.
button = Button(window, text="Payant", command=do_something)
button.pack()

window.mainloop()
