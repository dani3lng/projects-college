# Encryption Module
# Written by Cthulhu
# September 24, 2017

# This module contains functions that aid in encrypting/ decrypting files.
# NOTE: Under no circumstances should you actually use this program to
# encrypt sensitive information.  This basic program is for educational
# purposes only.

import random
import pickle

# generate_encryption takes no arguments and doesn't return anything.  The
# output of the function is to a file called not_suspicious.txt

def generate_encryption():
    # The ASCII characters we care about all have values between 32 and 126
    # EXCEPT the newline character which has a numerical value of 10.
    inds = list(range(32,127)) + [10]
    inds = random.sample(inds, len(inds))  # Shuffle the contents of inds list
    
    # Fill in the dictionary with shuffled characters
    codes = {}
    for i in range(len(inds) - 1):
        codes[chr(i+32)] = chr(inds[i])
    codes[chr(10)] = chr(inds[-1])
    
    # Open the file to store the dictionary in binary write mode
    encrypt_key = open('not_suspicious.txt', 'wb')  # This file name will
                                                    # surely trick any data
                                                    # thieves. ;)
    # Write the encryption dictionary to the file
    pickle.dump(codes, encrypt_key)
    
    # Close the file
    encrypt_key.close()
    
# get_encryption takes no arguments and returns a dictionary    
    
def get_encryption():
    # Open the file containing the encryption dictionary
    key_file = open('not_suspicious.txt', 'rb')
    
    # Load its contents into the variable key
    key = pickle.load(key_file)
    
    # Close the file
    key_file.close()
    
    # Return the dictionary stored in key
    return key