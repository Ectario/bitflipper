#!/usr/bin/env python3

from aes_cbc_bitflip import flipper
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-H','--hash', type=str, help='AES hash of the plaintext', required=True)
parser.add_argument('-t', '--text', type=str, help='Plaintext of the hash given', required=True)
parser.add_argument('-g', '--goal', type=str, help='Plaintext wanted after the decryption of the futur result', required=True)
parser.add_argument('-s', '--block-size', type=int, help='(optionally) size of each block in byte from the AES-CBC', required=False)
parser.add_argument('-v', '--verbose', help='(optionally) flag to get some logs', required=False)

if __name__ == '__main__':
    args = parser.parse_args()
    cipher = args.hash
    plaintext = args.text
    wanted = args.goal
    block_size = 16
    verbose = False

    if args.block_size != None:
        block_size = args.block_size

    if args.verbose != None:
        verbose = args.verbose
        
    # plaintext = "message%3DFor%20a%20fullfilling%20experience%20embrace%20listen%20to%20new%20music%2E%20Pay%20attention%20to%20details%2C%20titles%20are%20important%2E%20And%20remember%2C%20music%20it%27s%20flipping%20amazing%26user%3Dmario"
    # wanted    = "message%3DFor%20a%20fullfilling%20experience%20embrace%20listen%20to%20new%20music%2E%20Pay%20attention%20to%20details%2C%20titles%20are%20important%2E%20And%20remember%2C%20music%20it%27s%20flipping%20amazing%26user%3Dadmin"

    # cipher = "7ef1121810e23401e05975d6cffa94d906017ce939e3dea21fe521c02a7cbd5527fb2ed399f34976d964c96bde609e33af4e29af8c55f2c556c0b072894b3bfb31377d370fe95b2f0851da405007a4fb1e6141dec130eedf5f918f9cb4912c0eff9be93948ecafce977c58831c6bdbd9330b1e50fce8c9d2af16c92cb1d6e1d8f50751a2be9e12aa0cd834f9e04e4a4deb33918c662b6f9ff91200371d131f0e61078ace01592b41cde297306d847c9cbfcf3def06ba836b73cb095202a50693bf453e49a1a58a3dc0f84f2605a2cbc0fc71a5a0b7de1219114c73f0dcee8a4c04511469b0b211839143a41636799d4f"

    # result =  7ef1121810e23401e05975d6cffa94d906017ce939e3dea21fe521c02a7cbd5527fb2ed399f34976d964c96bde609e33af4e29af8c55f2c556c0b072894b3bfb31377d370fe95b2f0851da405007a4fb1e6141dec130eedf5f918f9cb4912c0eff9be93948ecafce977c58831c6bdbd9330b1e50fce8c9d2af16c92cb1d6e1d8f50751a2be9e12aa0cd834f9e04e4a4deb33918c662b6f9ff91200371d131f0e61078ace01592b41cde297306d847c9cbfcf3def06ba836b73cb095202a50693bf453e49a1a58a3dc0f84f2a00bdcbc1fc71a5a0b7de1219114c73f0dcee8a4c04511469b0b211839143a41636799d4f

    print(flipper(plaintext, cipher, wanted, block_size, verbose))


    """
    
    ╰─$ ./main.py -H "7ef1121810e23401e05975d6cffa94d906017ce939e3dea21fe521c02a7cbd5527fb2ed399f34976d964c96bde609e33af4e29af8c55f2c556c0b072894b3bfb31377d370fe95b2f0851da405007a4fb1e6141dec130eedf5f918f9cb4912c0eff9be93948ecafce977c58831c6bdbd9330b1e50fce8c9d2af16c92cb1d6e1d8f50751a2be9e12aa0cd834f9e04e4a4deb33918c662b6f9ff91200371d131f0e61078ace01592b41cde297306d847c9cbfcf3def06ba836b73cb095202a50693bf453e49a1a58a3dc0f84f2605a2cbc0fc71a5a0b7de1219114c73f0dcee8a4c04511469b0b211839143a41636799d4f"  -t "message%3DFor%20a%20fullfilling%20experience%20embrace%20listen%20to%20new%20music%2E%20Pay%20attention%20to%20details%2C%20titles%20are%20important%2E%20And%20remember%2C%20music%20it%27s%20flipping%20amazing%26user%3Dmario" -g "message%3DFor%20a%20fullfilling%20experience%20embrace%20listen%20to%20new%20music%2E%20Pay%20attention%20to%20details%2C%20titles%20are%20important%2E%20And%20remember%2C%20music%20it%27s%20flipping%20amazing%26user%3Dadmin" 


    7ef1121810e23401e05975d6cffa94d906017ce939e3dea21fe521c02a7cbd5527fb2ed399f34976d964c96bde609e33af4e29af8c55f2c556c0b072894b3bfb31377d370fe95b2f0851da405007a4fb1e6141dec130eedf5f918f9cb4912c0eff9be93948ecafce977c58831c6bdbd9330b1e50fce8c9d2af16c92cb1d6e1d8f50751a2be9e12aa0cd834f9e04e4a4deb33918c662b6f9ff91200371d131f0e61078ace01592b41cde297306d847c9cbfcf3def06ba836b73cb095202a50693bf453e49a1a58a3dc0f84f2a00bdcbc1fc71a5a0b7de1219114c73f0dcee8a4c04511469b0b211839143a41636799d4f
    
    
    """