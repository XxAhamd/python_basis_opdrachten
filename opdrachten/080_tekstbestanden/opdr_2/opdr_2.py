# Opdracht 2 tekstbestanden
# Naam student:
# Groep:

# De rest moet jij doen.....

import random

def raad_een_nummer():
    geheim_getal = random.randint(1, 100)
    aantal_pogingen = 0

    while True:
        geraden_getal = int(input("Raad mijn geheime getal: "))
        aantal_pogingen += 1

        if geraden_getal < geheim_getal:
            print("hoger")
        elif geraden_getal > geheim_getal:
            print("lager")
        else:
            print(f"Je hebt het getal geraden! Het is {geheim_getal}!")
            print(f"Je hebt het in {aantal_pogingen} keer geraden.")
            break

raad_een_nummer()
