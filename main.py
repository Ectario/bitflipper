#!/usr/bin/env python3

from aes_cbc_bitflip import flipper
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-H','--hash', type=str, help='AES hash of the plaintext', required=True)
parser.add_argument('-t', '--text', type=str, help='Plaintext of the hash given', required=True)
parser.add_argument('-g', '--goal', type=str, help='Plaintext wanted after the decryption of the futur result', required=True)
parser.add_argument('-s', '--block-size', type=int, help='(optionally) size of each block in byte from the AES-CBC', required=False)
parser.add_argument('-v', '--verbose',action='store_true', help='(optionally) flag to get some logs', required=False)

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
        

    print("NEW HASH :",flipper(plaintext, cipher, wanted, block_size, verbose))


    """
    
    ╰─$ ./main.py -H "618be3a451f64dd93551de33e18f444f4d50e6226cf2cf3bdf0d2928a6c560973bbb504ab87e94772b8d7ab768f01764"  -t "hello my name is a small test :)" -g "hello my name is a small success" 
    
    
    """