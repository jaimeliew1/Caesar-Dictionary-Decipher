import unittest
from CaesarDictionaryDecipher import dictDecipher, caesar

class Test(unittest.TestCase):

    def test_caesar_cipher(self):
        In = ['Hello this is a test',
              'This String Has Many 55 Unusual !@#$%^&*() Characters!?']
        shift = [5, 22]
        Out = ['MJQQT YMNX NX F YJXY',
               'PDEO OPNEJC DWO IWJU 55 QJQOQWH !@#$%^&*() YDWNWYPANO!?']

        for i, o, s in zip(In, Out, shift):
            self.assertEqual(caesar(i, s), o)

    def test_dictionary_decipher(self):
        In = 'LZAK AK S LWKL'
        Out = 'THIS IS A TEST'

        self.assertEqual(dictDecipher(In), Out)


    def test_dictionary_decipher_with_unusual_characters(self):
        In = 'MRHIIH, XLMW ASVH-WIRXIRGI LEW WXVERKI GLEVEGXIVW?! )(*&^12346'
        Out = 'INDEED, THIS WORD-SENTENCE HAS STRANGE CHARACTERS?! )(*&^12346'

        self.assertEqual(dictDecipher(In), Out)

if __name__ == '__main__':
    unittest.main()