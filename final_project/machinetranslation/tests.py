''' unit testing '''
import unittest
from translator import english_to_french, french_to_english

class TestEngtoFren(unittest.TestCase):
    ''' English to French '''
    def test1(self):
        ''' test '''
        self.assertEqual(english_to_french(''), '')
        self.assertEqual(english_to_french('Hello'),'Bonjour')

class TestFrentoEng(unittest.TestCase):
    ''' French to English '''
    def test1(self):
        ''' test '''
        self.assertEqual(french_to_english(''), '')
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        
