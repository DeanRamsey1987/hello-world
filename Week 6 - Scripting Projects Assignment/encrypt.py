import string

# Get all printable characters
chars = string.printable
n = len(chars)

# Input
plaintext = input("Enter a line of text to encrypt: ")
distance = int(input("Enter the distance value: "))

# Encrypt
encrypted = ""
for ch in plaintext:
    if ch in chars:
        new_index = (chars.index(ch) + distance) % n
        encrypted += chars[new_index]
    else:
        encrypted += ch  # Just in case of unexpected characters

# Output encrypted
print("Encrypted text:", encrypted)
