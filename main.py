#!/usr/bin/env python3

from aes_cbc_bitflip import get_blocks, get_indexes, get_block_nb_by_index
from checker import check_same_block

plaintext = "message%3DFor%20a%20fullfilling%20experience%20embrace%20listen%20to%20new%20music%2E%20Pay%20attention%20to%20details%2C%20titles%20are%20important%2E%20And%20remember%2C%20music%20it%27s%20flipping%20amazing%26user%3Dmario"
wanted    = "message%3DFor%20a%20fullfilling%20experience%20embrace%20listen%20to%20new%20music%2E%20Pay%20attention%20to%20details%2C%20titles%20are%20important%2E%20And%20remember%2C%20music%20it%27s%20flipping%20amazing%26user%3Dadmin"
indexes = get_indexes(plaintext, wanted, 16)


print(plaintext[indexes[0]:indexes[1]+1])
print(wanted[indexes[0]:indexes[1]+1])
print()