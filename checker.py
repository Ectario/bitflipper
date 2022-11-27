#!/usr/bin/env python3

def check_same_block(index_begin, index_end, block_size=16):
    """
    Given a block size, check if the two indices are in the same block
    
    :param index_begin: the index of the first element to change in the plaintext
    :param index_end: the index of the boundary (excluded!)
    :param block_size: the size of the block to be checked, defaults to 16 (optional)
    """
    if index_end - index_begin > block_size:
        return False

    return index_begin // block_size == index_end // block_size

def check_egality_length(plaintext, wanted):
    """
        It checks if the length of the plaintext is equal to the length of the wanted text

        :param plaintext: the text to be encrypted
        :param wanted: the string we want to encrypt
        :return: true if the check is validated.
    """    
    return len(plaintext) == len(wanted)