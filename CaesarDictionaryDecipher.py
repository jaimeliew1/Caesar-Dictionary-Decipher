# -*- coding: utf-8 -*-
"""
Caesar Dictionary Decipher
--------------------------

Decodes a Caesar cipher without knowing the shift index by using a dictionary
lookup.

@author: Jaime Liew
"""
# Load Dictionary
with open('words_alpha.txt') as f:
    Dictionary = [x.upper() for x in f.read().split('\n')]

def caesar(string, shift):
    # Returns a caesar cipher for a given shift index
    # Parameters
    # string: the string to cipher
    # shift: the shift index
    #
    # Returns: the ciphered string.

    cipher = [ord(x) for x in string.upper()]
    out = ''
    for c in cipher:
        if 65<=c<=90:
            out += chr(65 + (c-65+shift)%26)
        else:
            out += chr(c)
    return out

def dictDecipher(string, delim=' '):
    # finds the caesar cypher with the most words in the dictionary and
    # returns that.

    scoremax, bestShift = 0, 0
    for i in range(26):
        cipher = caesar(string, i)
        score = sum(word in Dictionary for word in cipher.split(delim))
        if score > scoremax:
            scoremax, bestShift = score, i

    return caesar(string, bestShift)


if __name__ == '__main__':
    string = 'HDTR. B PBEE LXX RHN TM RHNKL. LTOX LHFX LITSEX YHK FX :)'
    out = dictDecipher(string)
    print(out)


