# Opdracht 1 functies
# Naam student:
# Groep:


def write_to_file(afile, atext):
    # je code komt hier
    # het woordje pass hieronder kun je weghalen
   with open(afile, "a") as file:
        file.write(atext + "\n")

my_tekst = "Schrijf dit maar even in een bestandje"
my_file = "test.txt"
write_to_file(my_file, my_tekst)
