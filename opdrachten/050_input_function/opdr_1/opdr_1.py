# Opdracht 1 input function
# Naam student:
# Groep:

# Hier komt je code, maak gebruik van de input functie om de lengte van de rechthoekzijden van de driehoek op te vragen.

import math

def bereken_schuine_zijde(zijde1, zijde2):
    return math.sqrt(zijde1**2 + zijde2**2)

# Vraag de gebruiker om de lengte van de eerste zijde
zijde1 = float(input("Geef de lengte van de eerste zijde\n"))

# Vraag de gebruiker om de lengte van de tweede zijde
zijde2 = float(input("Geef de lengte van de tweede zijde\n"))

# Bereken de lengte van de schuine zijde
schuine_zijde = bereken_schuine_zijde(zijde1, zijde2)

# Toon het resultaat
print(f"\nDe lengte van de schuine zijde is: {schuine_zijde}")

