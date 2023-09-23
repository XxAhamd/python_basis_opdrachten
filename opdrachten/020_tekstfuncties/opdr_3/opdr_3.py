# Opdracht 3 tekstfuncties
# Naam student:
# Groep:

# Hier komt je code...
def draw_christmas_tree():
    for i in range(1, 6):
        spaces = " " * (5 - i)
        stars = "*" * (2 * i - 1)
        for _ in range(3):
            print(spaces + stars + spaces)

# Roep de functie aan om vijf bomen naast elkaar te tekenen
for _ in range(5):
    draw_christmas_tree()
