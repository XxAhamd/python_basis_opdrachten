# Opdracht 2 berekeningen
# Naam student:
# Groep:

# Hier komt je code...
# Functie om Celsius naar Fahrenheit om te rekenen
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Functie om Fahrenheit naar Celsius om te rekenen
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Gegeven temperaturen
c1 = -12
f1 = 144
c2 = 62.2
f2 = 96

# Berekeningen en uitvoer
print(f"{c1} graden Celsius is gelijk aan {celsius_to_fahrenheit(c1):.1f} graden Fahrenheit")
print(f"{f1} graden Fahrenheit is gelijk aan {fahrenheit_to_celsius(f1):.1f} graden Celsius")
print(f"{c2} graden Celsius is gelijk aan {celsius_to_fahrenheit(c2):.1f} graden Fahrenheit")
print(f"{f2} graden Fahrenheit is gelijk aan {fahrenheit_to_celsius(f2):.1f} graden Celsius")
