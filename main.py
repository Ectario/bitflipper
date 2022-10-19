#!/usr/bin/env python3

import aes_cbc_bitflip
from checker import check_same_block

plaintext = "message%3DFor%20a%20fullfilling%20experience%20embrace%20listen%20to%20new%20music%2E%20Pay%20attention%20to%20details%2C%20titles%20are%20important%2E%20And%20remember%2C%20music%20it%27s%20flipping%20amazing%26user%3Dmario"
wanted = "message%3DFor%20a%20fullfilling%20experience%20embrace%20listen%20to%20new%20music%2E%20Pay%20attention%20to%20details%2C%20titles%20are%20important%2E%20And%20remember%2C%20music%20it%27s%20flipping%20amazingllohellohellohe"
indexes = aes_cbc_bitflip.get_indexes(plaintext, wanted)
print(indexes)
print()
print(check_same_block(indexes[0], indexes[1] + 1))