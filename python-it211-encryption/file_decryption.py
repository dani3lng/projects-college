#File Decryption

import file_key

encrypt_dict = file_key.get_encryption()

encrypt_file = open('test_encrypted.txt', 'r')

encrypted_text = encrypt_file.read()

kv_pairs = list(encrypt_dict.items())

deencrypted_text = ''
for ch in reversed(encrypted_text.upper()):
    for i in range(len(kv_pairs)):
        if kv_pairs[i][1] == ch:
            index = i
            deencrypted_text += kv_pairs[index][0]

encrypt_file.close()
print(deencrypted_text)