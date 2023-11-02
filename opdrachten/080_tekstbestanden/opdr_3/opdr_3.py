# Opdracht 3 Tekst opslaan
# Naam student:
# Groep:



def caesar_cypher(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_value = 97 if char.islower() else 65
            encrypted_text += chr((ord(char) - shift_value + shift) % 26 + shift_value)
        else:
            encrypted_text += char
    return encrypted_text

# Voorbeeld van het gebruik van encryptie
input_text = input("Geef de tekst die je wilt encrypten: ")
encrypted = caesar_cypher(input_text, 5)
print("Geëncrypteerde tekst:", encrypted)

# Voorbeeld van het gebruik van decryptie
decrypted = caesar_cypher(encrypted, -5)
print("Gedecrypteerde tekst:", decrypted)
