import datetime

class Date:
    def __init__(self, jour, mois, annee):
        self.jour = jour
        self.mois = mois
        self.annee = annee

    def __str__(self):
        return f"{self.jour:02d}/{self.mois:02d}/{self.annee}"

    def est_passee(self):
        """Renvoie True si la date est passée, False sinon."""
        aujourd_hui = datetime.date.today()
        date_event = datetime.date(self.annee, self.mois, self.jour)
        return date_event < aujourd_hui


if __name__
