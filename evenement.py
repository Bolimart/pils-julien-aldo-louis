"""
objectif du fichier : création des 6 evenements déja enregistrer dans un sous
dossier evenement dans lequel sera enregistré les 6 évenements de base +
les evenements qu'on va creer par la suite qui seront actualiser et ajouter
dans ce sous dossier
creer un autre fichier et importer la class date


"""
from date import Date											

class Evenement:
    def __init__(self, nom_evenement, place_evenement, date_evenement, contact_evenement, prix_evenement): 
        self.nom = nom_evenement
        self.place = place_evenement
        self.date = date_evenement
        self.contact = contact_evenement
        self.prix = prix_evenement

    def nommer (self):
        print(f"le nom de l'evenement que vous avez choisis est {self.nom}")

    def place (self):
        print(f"la place de l'evenement que vous avez choisis est {self.place}")

    def date (self) :
        print(f" la date que vous avez choisis pour votre evenement est {self.date}")

    def contact (self) :
        print(f" le contact que vous avez choisis pour votre evenement est {self.contact}")

    def prix (self) :
        print(f" le prix que vous avez déterminé pour votre evenement est {self.prix}")

    def __str__(self):
        return f"{self.nom} au {self.place} le {self.date}. GRATUIT = {self.prix}. CONTACT: {self.contact}"
        

def CreerID(dataDict, num = 0):
    try:
        dataDict[f'{num}']
    except:
        return num
    else:
        return CreerID(dataDict, num + 1)
    
        
def CreerEvenement(dataDict, nom_evenement: str, place_evenement:str, date_evenement: Date, contact_evenement: str, prix_evenement: bool):
    id = CreerID(dataDict)
    print(id)
    dataDict[id] = Evenement(nom_evenement, place_evenement, date_evenement, contact_evenement, prix_evenement)


def CreerEvenement(dataDict, id: int, nom_evenement: str, place_evenement:str, date_evenement: Date, contact_evenement: str, prix_evenement: bool):
    dataDict[id] = Evenement(nom_evenement, place_evenement, date_evenement, contact_evenement, prix_evenement)
