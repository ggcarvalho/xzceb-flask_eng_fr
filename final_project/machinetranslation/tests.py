import unittest
from translator import english_to_french, french_to_english


class TestTranslateFunctions(unittest.TestCase):
    def test_null(self):
        self.assertEqual(english_to_french(None), None)
        self.assertEqual(french_to_english(None), None)

    def test_hello(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertEqual(french_to_english('Bonjour'),'Hello' )

    def test_oui(self):
        self.assertEqual(english_to_french('Yes'), 'Oui')
        self.assertEqual(french_to_english('Oui'), 'Yes' )

    def test_goodbye(self):
        self.assertEqual(english_to_french('Goodbye'), 'Au revoir')
        self.assertEqual(french_to_english('Au revoir'),'Goodbye' )

if __name__ == '__main__':
    unittest.main()