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

def caesarCipher(string, shift):
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

def caesarDictionaryDecipher(original):
    # finds the caesar cypher with the most words in the dictionary and
    # returns that.

    scoremax = 0
    bestShift = 0
    for i in range(26):
        score = 0
        string = caesarCipher(original, i)

        for word in string.split(' '):
            if word in Dictionary:
                score += 1
        if score > scoremax:
            scoremax, bestShift = score, i

    return caesarCipher(original, bestShift)


if __name__ == '__main__':
    string = 'HDTR. B PBEE LXX RHN TM RHNKL. LTOX LHFX LITSEX YHK FX :)'
    out = caesarDictionaryDecipher(string)
    print(out)


