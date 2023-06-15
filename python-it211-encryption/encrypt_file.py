# encrypts_a_file.py
# Written by Cthulhu
# September 24, 2017

# This program encrypts the file text.txt using a randomly generated
# encryption dictionary.

import encryption

# Generate an encryption dictionary and store it in a file
encryption.generate_encryption()

# Load the encryption dictionary
encrypt_dict = encryption.get_encryption()

# Open the file to encrypt and the file to write the encrypted text to
input_file = open('text.txt', 'r')
output_file = open('encrypted_text.txt', 'w')

# Read in the text from the file to encrypt
entire_text_file = input_file.read()

# Generate encrypted text as a string
encrypted_text = ''
for ch in entire_text_file:
    encrypted_text += encrypt_dict[ch]

# Write the encrypted text to a file
output_file.write(encrypted_text)

# Close both files
input_file.close()
output_file.close()