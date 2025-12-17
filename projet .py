"""
objectif du fichier : création des 6 evenements déja enregistrer dans un sous
dossier evenement dans lequel sera enregistré les 6 évenements de base +
les evenements qu'on va creer par la suite qui seront actualiser et ajouter
dans ce sous dossier
creer un autre fichier et importer la class date


"""
												

class Evenement:
    def __init__(self, nom_evenement, place_evenement, date_evenement, contact_evenement, prix_evenement): 
        self.nom_evenement = nom_evenement
        self.place_evenement = place_evenement
        self.date_evenement = date_evenement
        self.contact_evenement = contact_evenement
        self.prix_evenement = prix_evenement

    def nommer (self):
        print(f"le nom de l'evenement que vous avez choisis est {self.nom_evenement}")

    def place (self):
        print(f"la place de l'evenement que vous avez choisis est {self.place_evenement}")

    def date (self) :
        print(f" la date que vous avez choisis pour votre evenement est {self.date_evenement}")

    def contact (self) :
        print(f" le contact que vous avez choisis pour votre evenement est {self.contact_evenement}")

    def prix (self) :
        print(f" le prix que vous avez déterminé pour votre evenement est {self.prix_evenement}")
        

    
        
