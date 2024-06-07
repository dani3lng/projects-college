#Encryption dictionary and Encryption

import pickle

#create encryption dictionary
def generate_encryption():
    #create dictionary
    codes = {'A':'~', 'B':'!', 'C':'@', 'D':'#',
            'E':'$', 'F':'%', 'G':'^', 'H':'&', 
             'I':'*', 'J':'(',  'K':')',  'L':'-',
             'M':'_','N':'+', 'O':'[',  'P':']',
             'Q':'1', 'R':'2',  'S':'3', 'T':'4', 
             'U':'5', 'V':'6',  'W':'7',  'X':'8',
             'Y':'9','Z':'0'}
    #open file to store the dictionary in binary write mode
    key = open('encryptkey.txt', 'wb')
    #write the encryption dictionary to the file
    pickle.dump(codes,key)
    #close the file

#get_encryption takes no arguments and returns a dictionary
def get_encryption():
    #open file
    file = open('encryptkey.txt', 'rb')
    #load contents
    key = pickle.load(file)
    #close file
    file.close()
    #return dictionary
    return key

#generate encryption dictionary
generate_encryption()
#load encryption dictionary
encrypt_dict = get_encryption()
#open file to encrypt and create write file
input_file = open('test.txt', 'r')
output_file = open('test_encrypted.txt', 'w')
#read text from file to encrypt
test_file = input_file.read().upper()
#generate encrypted text as string
codes = encrypt_dict
test_encrypted = ''
for ch in test_file:
    if ch in codes:
        test_encrypted += codes[ch]
    else:
        test_encrypted += ch
#write encrypted text to file
output_file.writelines(reversed(test_encrypted))
#close both files
input_file.close()
output_file.close()