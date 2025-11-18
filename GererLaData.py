

class Evenement:
        def __init__(self, nom, date, place, prix, contact):
            self.nom = nom
            self.date = date
            self.place = place
            self.prix = prix
            self.contact = contact


def Sauver(e: Evenement):
    with open("pils-aldo-louis-julien-2026-01/donnees/evenements.txt", "a") as f:
        f.write(f"\n{e.nom},{e.date},{e.place},{e.prix},{e.contact}")


def Charger():
    Data = {}
    with open("pils-aldo-louis-julien-2026-01/donnees/evenements.txt", "r") as f:
          
        for line in f.readlines():
            if "nom" in line:
                pass
            else:
                p = line.split(',')
                Data[p[0]] = Evenement(p[0], p[1], p[2], p[3], p[4])
        return Data
               


if __name__ == '__main__':

    d = Charger()

    for k, d in d.items():
        print(k)

    #Sauver()