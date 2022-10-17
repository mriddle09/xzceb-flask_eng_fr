import unittest
import sys
sys.path.append('../machinetranslation')
from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):

    def test_e2f(self):
        self.assertEqual('Bonjour', english_to_french('Hello'))
        self.assertEqual('Oui', english_to_french('Yes'))
        self.assertEqual('no input', english_to_french(''))
    
    def test_f2e(self):
        self.assertEqual('Hello', french_to_english('Bonjour'))
        self.assertEqual('Yes', french_to_english('Oui'))
        self.assertEqual('no input', french_to_english(''))

unittest.main()