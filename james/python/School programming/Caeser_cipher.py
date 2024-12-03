alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
original = str(input("Enter the text to encrypt: ")).upper()
key = int(input("Enter the key: "))

print("")

deciphered_text = []
for letter in original:

    original_index = alphabet.index(letter)


    encrypted_index = original_index + key

    encrypted_character = alphabet[encrypted_index]
    print(f"encrypted character is {encrypted_character}")

    deciphered_text.append(encrypted_character)

print("")
print("the encrypted string is " + "".join(deciphered_text))
print("")

print(f"original index is {original_index} ")
print(f"encrypted index is {encrypted_index}")
print("")