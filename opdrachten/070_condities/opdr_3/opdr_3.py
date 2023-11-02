# Opdracht 3 condities
# Naam student:
# Groep:




normale_toegangsprijs = 12.50
kortings_percentages = {"baby": 100, "kinderen": 50, "volwassenen": 0, "ouderen": 30}
leeftijd = {"baby": (0, 2), "kinderen": (3, 18), "volwassenen": (19, 64), "ouderen": (65, 150)}

# Hier komt je code...
leeftijd_input = int(input("Geef uw leeftijd in aantal jaar: "))

for groep, leeftijdsgrenzen in leeftijd.items():
    if leeftijdsgrenzen[0] <= leeftijd_input <= leeftijdsgrenzen[1]:
        korting = kortings_percentages[groep]
        print(f"U behoort tot de groep {groep}")
        print(f"U krijgt {korting}% korting")
        prijs_met_korting = normale_toegangsprijs - (normale_toegangsprijs * korting / 100)
        print(f"U betaalt daarom {prijs_met_korting:.2f}")
        break