#!/usr/bin/env python3

from checker import *

def get_indexes(plaintext_given, plaintext_wanted):
    index_begin_diff = None
    index_end_diff = None
    for i, elmt in enumerate(plaintext_given):
        if index_begin_diff == None and plaintext_wanted[i] != elmt:
            index_begin_diff = i
            index_end_diff = i
        elif plaintext_wanted[i] != elmt:
            index_end_diff = i
        elif index_begin_diff != None:
            break
    return index_begin_diff, index_end_diff    

def get_blocks(msg, block_size, is_encrypted):
    """
    It takes a message, a block size, and a boolean value indicating whether the message is encrypted or
    not, and returns a list of blocks of the message
    
    :param msg: the message to be split into blocks
    :param block_size: the size of the block in bytes
    :param is_encrypted: True if the message is encrypted, False if it's plaintext
    :return: A list of blocks of the message, each block is of size block_size.
    """
    msg_blocks = []
    tmp = ""
    factor = 2 if is_encrypted else 1 # if encrypted then it's hexadecimal, which is encoded by 2 char for 1 byte
    for i in range(1,len(msg)+1):
        tmp += msg[i-1]
        if i % (block_size*factor) == 0:
            msg_blocks.append(tmp)
            tmp = ""
    if tmp != "": 
        msg_blocks.append(tmp)
    return msg_blocks

def flipper(plaintext_given, ciphertext, plaintext_wanted, block_size=16, log=False):
    if log:
        print("Message chunks : \n")
    msg_blocks = get_blocks(plaintext_given, block_size, False)
    if log:
        print(msg_blocks)
    check_same_block(plaintext_given, plaintext_wanted, block_size)
    msg_blocks_enc = get_blocks(ciphertext, block_size, True)
    if log:
        print()
        print(msg_blocks_enc)
    msg_blocks_enc_list = [list(i) for i in msg_blocks_enc]