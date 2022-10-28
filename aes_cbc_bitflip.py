#!/usr/bin/env python3

from checker import *

def get_indexes(plaintext_given, plaintext_wanted, block_size):
    """
    It returns the first and last index of the first difference between two strings
    
    :param plaintext_given: the plaintext that you have
    :param plaintext_wanted: the plaintext you want to get
    :return: The indexes of the first and last different characters between the two strings.
    """
    
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
    i = index_end_diff
    while get_block_nb_by_index(i, block_size) == get_block_nb_by_index(i-1,block_size):
        if plaintext_wanted[i] != plaintext_given[i]:
            index_end_diff = i
        i+=1
    return index_begin_diff, index_end_diff    

def get_block_nb_by_index(index, block_size):
    """
    It returns the block number of a given index
    
    :param index: the index of the element in the array
    :param block_size: the size of the block
    :return: The block number of the block that contains the given index.
    """
    return index // block_size

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
    if not check_egality_length(plaintext_given, plaintext_wanted):
        raise Exception("The plaintext given haven't the same length than the plaintext wanted")

    if log:
        print("[!] Message blocks : \n")
        print()

    msg_blocks = get_blocks(plaintext_given, block_size, False)

    if log:
        print(msg_blocks)

    indexes = get_indexes(plaintext_given, plaintext_wanted, block_size)

    if not check_same_block(indexes[0], indexes[1], block_size):
        raise Exception("Can't execute the bit flipping, the differences aren't in the same block => bit flipping impossible")

    msg_blocks_enc = get_blocks(ciphertext, block_size, True)

    if log:
        print()
        print("[!] Msg blocks enc :\n")
        print(msg_blocks_enc)
        print()

    msg_blocks_enc_list = [list(i) for i in msg_blocks_enc]

    block_nb = get_block_nb_by_index(indexes[0], block_size)
    starting_index = (indexes[0] % block_size) *2
    ending_index = (indexes[1] % block_size + 1) *2
    index_text = indexes[0]

    if log:
        print("\n\n-- Trace of byte changed --\n")

    for i in range(starting_index, ending_index, 2):
        if log:
            print("index", i, "    ->    ", msg_blocks_enc[block_nb][i:i+2], "    in     ", msg_blocks_enc[block_nb])
            print("index char", index_text, "    ->    ", plaintext_given[index_text], " replaced by ", plaintext_wanted[index_text])

        msg_enc_l = int(msg_blocks_enc[block_nb - 1][i:i+2],16)
        letter_to_replace = ord(plaintext_given[index_text])
        letter_by_what_to_replace = ord(plaintext_wanted[index_text])
        calculus = letter_to_replace ^ msg_enc_l ^ letter_by_what_to_replace
        r = hex(calculus).replace("0x", "").zfill(2)
        msg_blocks_enc_list[block_nb - 1][i] = r[0]
        msg_blocks_enc_list[block_nb - 1][i+1] = r[1]
        index_text+=1

    msg_blocks_enc = ["".join(i) for i in msg_blocks_enc_list]
    final_payload = "".join(msg_blocks_enc)
    return final_payload