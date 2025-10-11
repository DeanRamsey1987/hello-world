import string

# Get all printable characters
chars = string.printable
n = len(chars)

# Input
ciphertext = input("Enter the text to decrypt: ")
distance = int(input("Enter the distance value: "))

# Decrypt
decrypted = ""
for ch in ciphertext:
    if ch in chars:
        new_index = (chars.index(ch) - distance) % n
        decrypted += chars[new_index]
    else:
        decrypted += ch

# Output
print("Decrypted text:", decrypted)
