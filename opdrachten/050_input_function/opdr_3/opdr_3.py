# Opdracht 3 input functie
# Naam student:
# Groep:

# Hier komt je code...

# Vraag de gebruiker om steden in te voeren, gescheiden door komma's
input_steden = input("Voer minimaal 5 steden in, gescheiden door komma's: ")

# Splits de ingevoerde tekst op komma's en verwijder eventuele extra spaties
stedenlijst = [stad.strip() for stad in input_steden.split(',')]

# Sorteer de lijst in omgekeerde volgorde
stedenlijst.sort(reverse=True, key=lambda x: x.lower())

# Print de gesorteerde lijst
print(stedenlijst)
