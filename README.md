# bitflipper

bitflipper - Uses bit-flipping to modify an AES-CBC cipher

[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](http://www.gnu.org/licenses/gpl-3.0)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/PyCryptodome)

# Description

bitflipper allows you to modify an encryption created by the AES-CBC algorithm to obtain a new one which, when deciphered, allows us to obtain a chosen plaintext.

# Requirements

- [Python 3](https://www.python.org/downloads/)
- (optionnal for tests) [PyCryptodome (python 3 module)](https://pypi.org/project/PyCryptodome/)

# Installation

## Download

The files can either be downloaded directly (the download zip in the clone menu) or can be cloned if you have git available:

 `git clone https://github.com/Ectario/bitflipper.git`

## Setup

Go to the bitflipper directory: `cd bitflipper`.

To authorize the execution of the code under macOS/Linux: `chmod +x ./main.py`

_note: for Windows systems you just have to make sure that python3 is in the path_

# Usage

### General usage (macOS/Linux): `./main.py -H <cipher_text> -t <plain_text> -g <goal_text> [OPTIONS...]`
_note: under Windows there are the same commands but without './'_

Of course it is possible to chain as many options as you want.

# Example

- With verbose mode :

```sh
        ╰─$ ./main.py -H 618be3a451f64dd93551de33e18f444f4d50e6226cf2cf3bdf0d2928a6c560973bbb504ab87e94772b8d7ab768f01764 -t "hello my name is a small test :)" -g "hello my name is a small success" -v
        
        [!] Message blocks : 

        ['hello my name is', ' a small test :)']

        [!] Msg blocks enc :

        ['618be3a451f64dd93551de33e18f444f', '4d50e6226cf2cf3bdf0d2928a6c56097', '3bbb504ab87e94772b8d7ab768f01764']


        -- Trace of byte changed --

        index 18     ->     0d     in      4d50e6226cf2cf3bdf0d2928a6c56097
        index char 25     ->     t  replaced by  s
        index 20     ->     29     in      4d50e6226cf2cf3bdf0d2928a6c56097
        index char 26     ->     e  replaced by  u
        index 22     ->     28     in      4d50e6226cf2cf3bdf0d2928a6c56097
        index char 27     ->     s  replaced by  c
        index 24     ->     a6     in      4d50e6226cf2cf3bdf0d2928a6c56097
        index char 28     ->     t  replaced by  c
        index 26     ->     c5     in      4d50e6226cf2cf3bdf0d2928a6c56097
        index char 29     ->        replaced by  e
        index 28     ->     60     in      4d50e6226cf2cf3bdf0d2928a6c56097
        index char 30     ->     :  replaced by  s
        index 30     ->     97     in      4d50e6226cf2cf3bdf0d2928a6c56097
        index char 31     ->     )  replaced by  s

        NEW HASH : 618be3a451f64dd93556ce23f6ca0d154d50e6226cf2cf3bdf0d2928a6c560973bbb504ab87e94772b8d7ab768f01764
```

- Without verbose mode:

```sh

╰─$ ./main.py -H 618be3a451f64dd93551de33e18f444f4d50e6226cf2cf3bdf0d2928a6c560973bbb504ab87e94772b8d7ab768f01764 -t "hello my name is a small test :)" -g "hello my name is a small success"   

NEW HASH : 618be3a451f64dd93556ce23f6ca0d154d50e6226cf2cf3bdf0d2928a6c560973bbb504ab87e94772b8d7ab768f01764


```