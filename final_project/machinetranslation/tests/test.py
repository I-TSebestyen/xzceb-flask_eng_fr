import unittest
from translator import english_to_french, french_to_english


class TestEnglishToFrench(unittest.TestCase):
    def test_english_to_french(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertNotEqual(english_to_french(0), 'Bonjour')
        self.assertEqual(english_to_french('What is your name?'), 'Quel est votre nom?')


class TestFrenchToEnglish(unittest.TestCase):
    def test_french_to_english(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertNotEqual(french_to_english(0), 'Hello')
        self.assertEqual(french_to_english('Quelle heure est-il?'), 'What time is it?')


unittest.main()
