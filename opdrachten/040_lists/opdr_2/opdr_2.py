# Opdracht 2 lists
# Naam student:
# Groep:


rivier_info = { 
    "rijn": ["nederland", "duitsland", "Frankrijk"], 
    "maas": ["nederland", "belgië", "duitsland"], 
    "nijl": ["egypte", "soedan", "oeganda"] 
}

rivieren = list(rivier_info.keys())

# Eerste opdracht
print(f"De rivier {rivieren[0].capitalize()} stroomt onder andere door {rivier_info[rivieren[0]][1].capitalize()}")

# Tweede opdracht
print(f"De rivier {rivieren[1].capitalize()} stroomt onder andere door {rivier_info[rivieren[0]][0].capitalize()}")

# Derde opdracht
print(f"De rivier {rivieren[2].capitalize()} stroomt onder andere door {rivier_info[rivieren[0]][2].capitalize()}")
