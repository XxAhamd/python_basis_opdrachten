# Opdracht 1 lists
# Naam student:
# Groep:

# Maak een lijst aan
lijst = []

# Maak vier dictionaries voor personen en voeg ze toe aan de lijst
persoon1 = { "id": 1, "voornaam": "John", "achternaam": "Doe" }
persoon2 = { "id": 2, "voornaam": "Jane", "achternaam": "Smith" }
persoon3 = { "id": 3, "voornaam": "Alice", "achternaam": "Johnson" }
persoon4 = { "id": 4, "voornaam": "Bob", "achternaam": "Brown" }

lijst.append(persoon1)
lijst.append(persoon2)
lijst.append(persoon3)
lijst.append(persoon4)

# Geef de volledige naam van de tweede persoon weer
print(lijst[1]["voornaam"], lijst[1]["achternaam"])
