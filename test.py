#!/usr/bin/env python3

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

plaintext = "hello my name is a small test :)"
wanted = "hello my name is a small success"

key = get_random_bytes(16)
iv = get_random_bytes(16)

def encrypt(plaintext):
    aes = AES.new(key, AES.MODE_CBC, iv)
    plaintext_padded = pad(plaintext.encode('unicode_escape'), AES.block_size, style='pkcs7')
    ciphertext = aes.encrypt(plaintext_padded).hex()
    return ciphertext
    
def decrypt(ciphertext):
    aes = AES.new(key, AES.MODE_CBC, iv)
    plaintext_padded = aes.decrypt(bytes.fromhex(ciphertext))
    try:
        plaintext = unpad(plaintext_padded, AES.block_size, style='pkcs7').decode('unicode_escape')
    except ValueError as e:
        print(e)
        return plaintext_padded
    return plaintext



#######################################
from aes_cbc_bitflip import *
from checker import check_same_block

indexes = get_indexes(plaintext, wanted, 16)


print(plaintext[indexes[0]:indexes[1]+1])
print(wanted[indexes[0]:indexes[1]+1])
print()
#######################################


print("--------------------------------- Full result ---------------------------------")
ciphertext = encrypt(plaintext)
print(ciphertext)
cipher_modified = flipper(plaintext, ciphertext, wanted, 16, False)
print(decrypt(cipher_modified))
# print("\n\ncipher:", get_blocks(ciphertext, 16, True))
# print("\n\ncipher:", get_blocks(cipher_modified,16,True))

