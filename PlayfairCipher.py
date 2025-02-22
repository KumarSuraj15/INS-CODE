def create_matrix(key):
    # Remove duplicates and replace J with I
    key = key.upper().replace('J', 'I')
    key = "".join(sorted(set(key), key=key.index))

    # Create the matrix
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    matrix = [c for c in key if c in alphabet] + [c for c in alphabet if c not in key]

    return [matrix[i:i+5] for i in range(0, 25, 5)]

def find_position(matrix, char):
    for row_idx, row in enumerate(matrix):
        if char in row:
            return row_idx, row.index(char)
    return None

def prepare_text(text, for_encryption=True):
    text = text.upper().replace("J", "I")
    result = ""

    i = 0
    while i < len(text):
        a = text[i]
        b = text[i+1] if i + 1 < len(text) else ""

        if for_encryption and a == b:
            result += a + "X"
            i += 1
        elif b == "":
            result += a + "X"
            i += 1
        else:
            result += a + b
            i += 2

    return result

def encrypt_pair(pair, matrix):
    r1, c1 = find_position(matrix, pair[0])
    r2, c2 = find_position(matrix, pair[1])

    if r1 == r2:  # Same row
        return matrix[r1][(c1 + 1) % 5] + matrix[r2][(c2 + 1) % 5]
    elif c1 == c2:  # Same column
        return matrix[(r1 + 1) % 5][c1] + matrix[(r2 + 1) % 5][c2]
    else:  # Rectangle
        return matrix[r1][c2] + matrix[r2][c1]

def decrypt_pair(pair, matrix):
    r1, c1 = find_position(matrix, pair[0])
    r2, c2 = find_position(matrix, pair[1])

    if r1 == r2:  # Same row
        return matrix[r1][(c1 - 1) % 5] + matrix[r2][(c2 - 1) % 5]
    elif c1 == c2:  # Same column
        return matrix[(r1 - 1) % 5][c1] + matrix[(r2 - 1) % 5][c2]
    else:  # Rectangle
        return matrix[r1][c2] + matrix[r2][c1]

def playfair_encrypt(plaintext, key):
    matrix = create_matrix(key)
    plaintext = prepare_text(plaintext, for_encryption=True)

    ciphertext = ""
    for i in range(0, len(plaintext), 2):
        ciphertext += encrypt_pair(plaintext[i:i+2], matrix)

    return ciphertext

def playfair_decrypt(ciphertext, key):
    matrix = create_matrix(key)

    plaintext = ""
    for i in range(0, len(ciphertext), 2):
        plaintext += decrypt_pair(ciphertext[i:i+2], matrix)

    return plaintext

if __name__ == "__main__":
    key = input("Enter the key for Playfair Cipher: ")
    choice = input("Do you want to encrypt or decrypt? (e/d): ").lower()

    if choice == "e":
        plaintext = input("Enter the plaintext: ")
        ciphertext = playfair_encrypt(plaintext, key)
        print(f"Encrypted text: {ciphertext}")
    elif choice == "d":
        ciphertext = input("Enter the ciphertext: ")
        plaintext = playfair_decrypt(ciphertext, key)
        print(f"Decrypted text: {plaintext}")
    else:
        print("Invalid choice!")

