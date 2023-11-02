# Vragenlijst voor feestgangers
vragen = [
    "Wat is je voornaam?",
    "Wat is je achternaam?",
    "Wat neem je mee aan drank?",
    "Wat neem je mee om te eten?"
]

feestgangers = []  # Lijst om feestgangers op te slaan

while True:
    antwoorden = {}  # Dictionary om antwoorden van één feestganger op te slaan
    print("Beantwoord de volgende vragen:")
    for i, vraag in enumerate(vragen, 1):
        antwoord = input(f"{i}. {vraag}\n")
        antwoorden[vraag.split(" ")[-1].strip("?")] = antwoord  # Opslaan van antwoorden in de dictionary
    feestgangers.append(antwoorden)

    nog_een = input("Wil je nog een persoon toevoegen? (ja/nee): ")
    if nog_een.lower() != "ja":
        break

# Opslaan van antwoorden in een tekstbestand
bestandsnaam = "feestgangers.txt"

with open(bestandsnaam, "w") as bestand:
    for feestganger in feestgangers:
        bestand.write("----\n")
        for vraag, antwoord in feestganger.items():
            bestand.write(f"{vraag}: {antwoord}\n")
        bestand.write("\n")

print("Bedankt voor het invullen!")
print("See you at the party.")
