def generate_vigenere_table():
    table = []
    for i in range(26):
        row = [chr((i + j) % 26 + 65) for j in range(26)]
        table.append(row)
    return table

def vigenere_encrypt(plaintext, key):
    table = generate_vigenere_table()
    plaintext = plaintext.upper()
    key = key.upper()

    ciphertext = ""
    key_index = 0

    for char in plaintext:
        if char.isalpha():
            row = ord(key[key_index]) - 65
            col = ord(char) - 65
            ciphertext += table[row][col]
            key_index = (key_index + 1) % len(key)
        else:
            ciphertext += char

    return ciphertext

def vigenere_decrypt(ciphertext, key):
    table = generate_vigenere_table()
    ciphertext = ciphertext.upper()
    key = key.upper()

    plaintext = ""
    key_index = 0

    for char in ciphertext:
        if char.isalpha():
            row = ord(key[key_index]) - 65
            col = table[row].index(char)
            plaintext += chr(col + 65)
            key_index = (key_index + 1) % len(key)
        else:
            plaintext += char

    return plaintext

if __name__ == "__main__":
    key = input("Enter the key for Polyalphabetic Cipher: ")
    choice = input("Do you want to encrypt or decrypt? (e/d): ").lower()

    if choice == "e":
        plaintext = input("Enter the plaintext: ")
        ciphertext = vigenere_encrypt(plaintext, key)
        print(f"Encrypted text: {ciphertext}")
    elif choice == "d":
        ciphertext = input("Enter the ciphertext: ")
        plaintext = vigenere_decrypt(ciphertext, key)
        print(f"Decrypted text: {plaintext}")
    else:
        print("Invalid choice!")
