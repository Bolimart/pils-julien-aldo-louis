
class Recherche:

    def __init__(self, data):
        self.data = data

    def recherche(self, s):
        result = []

        for cle in self.data.keys():
            if cle[:len(s)] == s:
                result.append(("nom", self.data[cle]))
            else:
                event = self.data[cle]
                if event.prix[:len(s)] == s:
                    result.append(("prix", self.data[cle]))
                if event.date[:len(s)] == s:
                    result.append(("date", self.data[cle]))
                if event.place[:len(s)] == s:
                    result.append(("place", self.data[cle]))
                if event.contact[:len(s)] == s:
                    result.append(("contact", self.data[cle]))

            return result
                


if __name__ == "__main__":

    from GererLaData import *

    r = Recherche(Charger())

    res = r.recherche("2")

    for x in res:
        print(f"{x[0]} | {x[1].nom}")