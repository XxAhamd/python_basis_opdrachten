# Opdracht 3 input functie
# Naam student:
# Groep:

# Hier komt je code...

# Hier start de for-loop

# Lijst met pizza's
pizzas = ['margharita', 'calzone', 'verdi', 'olivio', 'quattro stagioni']

# Sorteer de lijst op alfabet
pizzas.sort()
print("Gesorteerde lijst:", pizzas)

# Voeg een nieuwe pizza toe
pizzas.append('yo-favorito')
print("Lijst na toevoegen:", pizzas)

# Verwijder de minst favoriete pizza
pizzas.remove('olivio')
print("Lijst na verwijderen:", pizzas)

# Print de eerste 3 pizza's
print("Eerste 3 pizza's:", pizzas[:3])

# Print alleen de middelste pizza
print("Middelste pizza:", pizzas[len(pizzas)//2])

# Print de laatste 3 pizza's
print("Laatste 3 pizza's:", pizzas[-3:])
