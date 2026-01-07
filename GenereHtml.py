
import GererLaData as g

eventTemplate = """    <div class="evenement">
          <p class="titre-event">{nom}</p>
          <p class="prix-event">{prix}</p>
          <p class="date-event">{date}</p>
          <p class="lieu-event">{lieu}</p>
          <p class="contact-event">{contact}</p>
        </div>
"""

def GenereHtml():
    data = g.Charger()

    with open("template.html", "r") as f:
        contents = f.readlines()

    for id, e in data.items():
        if e.date.est_passee(): continue
        temp = eventTemplate.format(nom=e.nom, prix="Gratuit" if e.prix else "Payant", date=e.date, lieu=e.place, contact=e.contact)
        contents.insert(19, temp)

    with open("index.html", "w") as f:
        f.writelines(contents)


if __name__ == '__main__':
    GenereHtml()

