# Decryption Program
# Written by Cthulhu
# September 24, 2017

# This program decrypts the file encrypted_text.txt using a randomly
# generated encryption dictionary.
import encryption
# Load and assign the encryption dictionary
encrypt_dict = encryption.get_encryption()

# Open the encrypted file in read mode
encrypted_file = open('encrypted_text.txt', 'r')

# Read in the contents of the encrypted file to a string
encrypted_text = encrypted_file.read()

# Create a list of tuples containing the key-value pairs in the encryption
# dictionary
key_value_pairs = list(encrypt_dict.items())

# Store the deencrypted text in a string
deencrypted_text = ''
for ch in encrypted_text:
    for i in range(len(key_value_pairs)):
        if key_value_pairs[i][1] == ch:
            index = i
    deencrypted_text += key_value_pairs[index][0]

# Close the file
encrypted_file.close()

# Display the deencrypted information
print(deencrypted_text)