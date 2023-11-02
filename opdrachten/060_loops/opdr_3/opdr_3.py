# Opdracht 3 input functie
# Naam student:
# Groep:

# Hier komt je code...

# Hier start de for-loop

my_list = []

# Loop van 3 tot 81 met stappen van 3
for i in range(3, 82, 3):
    # Bereken het kwadraat van i en deel door 3, voeg het resultaat toe aan de lijst
    resultaat = (i ** 2) / 3.0
    my_list.append(resultaat)

# Print de gevulde lijst op het scherm
print(my_list)
