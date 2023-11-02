# Opdracht 1 while-loops
# Naam student:
# Groep:

# Jouw code komt hier

# Enquête vragen
vragen = [
    "Wat vind je van de huidige regering?",
    "Wat vind je van de Python-lessen tot nu toe?",
    "Wat vind jij de mooiste stad van Nederland?"
]

# Leeg antwoordendict initialiseren
antwoorden = {}

# Loop door de vragen en verkrijg de antwoorden
for vraag in vragen:
    antwoord = input(vraag + " ")
    antwoorden[vraag] = antwoord

# Opslaan van antwoorden naar een tekstbestand
bestandsnaam = "enquete_resultaten.txt"

with open(bestandsnaam, "w") as bestand:
    for vraag, antwoord in antwoorden.items():
        bestand.write(f"{vraag}\n")
        bestand.write(f"{antwoord}\n")
        bestand.write("\n")

print("Bedankt voor het invullen van de enquête. De resultaten zijn opgeslagen in", bestandsnaam)
