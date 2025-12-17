
class Recherche:

    def __init__(self, data):
        self.data = data

    def recherche(self, s:str):
        result = []
        s = s.lower()

        if s in "gratuit":
            return self.filtrer_gratuit()

        for cle in self.data.keys():
            event = self.data[cle]
            if s in event.nom.lower():
                result.append(event)
            elif s in str(event.date):
                result.append(event)
            elif s in event.place.lower():
                result.append(event)
            elif s in event.contact.lower():
                result.append(event)

        return result
    
    def filtrer_gratuit(self):
        result = []

        for val in self.data.values():
            if val.prix:
                result.append(val)
        
        return result
                


if __name__ == "__main__":

    from GererLaData import *
    from evenement import *

    data = Charger()

    CreerEvenement(data, "Noël", "Mairie de La Roche sur Yon", "2025-12-22","info@mairieYon85.fr", True)

    r = Recherche(data)

    Sauver(data)

    res = r.recherche("gratuit")

    for x in res:
        print(x)