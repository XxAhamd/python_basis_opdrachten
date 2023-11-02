# Opdracht 1 functies
# Naam student:
# Groep:


def kilometers_naar_miles(km):
    miles = km / 1.609344
    return miles

def miles_naar_kilometers(miles):
    km = miles * 1.609344
    return km

# Voorbeeldgebruik van de functies
kilometers = 1223
miles = 867

km = kilometers_naar_miles(kilometers)
m = miles_naar_kilometers(miles)

print(f"{kilometers} kilometers = {km} miles")
print(f"{miles} miles = {m} kilometers")
