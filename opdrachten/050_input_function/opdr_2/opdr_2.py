# Opdracht 2 berekeningen
# Naam student:
# Groep:

# Hier komt je code...

# Maak een initiële lijst met gasten
gastenlijst = ["Ahmad", "Paul", "Kees", "Marie", "Hilda"]

# Print de initiële gastenlijst
print("Initiële gastenlijst:")
print(gastenlijst)

# Verwijder Marie uit de gastenlijst
gastenlijst.remove("Marie")

# Print de bijgewerkte gastenlijst zonder Marie
print("\nGastenlijst zonder Marie:")
print(gastenlijst)

# Voeg George toe naast Kees
kees_index = gastenlijst.index("Kees")
gastenlijst.insert(kees_index + 1, "George")

# Print de uiteindelijke gastenlijst met George naast Kees
print("\nUiteindelijke gastenlijst met George naast Kees:")
print(gastenlijst)
