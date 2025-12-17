

from evenement import Evenement
from date import Date


def SauverEvent(e: Evenement, id):
    with open("donnees/evenements.txt", "r") as f:
        f.readline()
        for i in f.readlines():
            print(f"compairing id {id} with {i[0]}")
            if int(i[0]) == id: 
                print(f"same id: {id}")
                return
    with open("donnees/evenements.txt", "a") as f:
        f.write(f"\n{id},{e.nom},{e.place},{str(e.date)},{e.contact},{'*' if e.prix else ''}")  
        print(f"event with id {id} succesfully added")


def Sauver(d):
    for id, e in d.items():
        id = int(id)
        SauverEvent(e, id)      


def Charger():
    Data = {}
    with open("donnees/evenements.txt", "r") as f:
        f.readline() # retire le header
        for line in f.readlines():
            p = line.split(',')

            d = p[3].split('-')
            date = Date(d[0], d[1], d[2])
            Data[p[0]] = Evenement(p[1], p[2], date, p[4], True if "*" in p[5] else False)
        return Data
               


if __name__ == '__main__':

    d = Charger()

    for k, d in d.items():
        print(d)

    #Sauver()