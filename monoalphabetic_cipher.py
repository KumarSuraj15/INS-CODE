# Monoalphabetic Cipher Implementation in Python with Switch-Case

def monoalphabetic_cipher(text, key, mode):
    # Define the alphabet
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    key = key.upper()

    if len(set(key)) != 26 or not key.isalpha():
        raise ValueError("Key must be a 26-character unique alphabet string.")

    def encrypt_char(char):
        if char.isalpha():
            idx = alphabet.index(char.upper())
            return key[idx] if char.isupper() else key[idx].lower()
        else:
            return char

    def decrypt_char(char):
        if char.isalpha():
            idx = key.index(char.upper())
            return alphabet[idx] if char.isupper() else alphabet[idx].lower()
        else:
            return char

    match mode:  # Using Python's match-case for switch-case behavior
        case 'encrypt':
            return ''.join(encrypt_char(char) for char in text)
        case 'decrypt':
            return ''.join(decrypt_char(char) for char in text)
        case _:
            raise ValueError("Invalid mode. Use 'encrypt' or 'decrypt'.")

# Main program for user input
if __name__ == "__main__":
    print("Monoalphabetic Cipher Program")
    text = input("Enter the text: ")
    key = input("Enter the 26-character key: ").strip()
    mode = input("Enter the mode ('encrypt' or 'decrypt'): ").strip().lower()

    try:
        result = monoalphabetic_cipher(text, key, mode)
        print(f"Result: {result}")
    except ValueError as e:
        print(e)