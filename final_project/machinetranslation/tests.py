import unittest

from translator import french_to_english,english_to_french

class test_f2e(unittest.TestCase): 
    def test1(self): 
        self.assertNotEqual(french_to_english(0), 0) 
    def test2(self):
        self.assertEqual(french_to_english('Nous'), 'We') 
    def test3(self):
         self.assertEqual(french_to_english('Bonjour'), 'Hello') 
class test_e2f(unittest.TestCase): 
    def test1(self): 
        self.assertNotEqual(english_to_french(0), 0) 
    def test2(self):
        self.assertEqual(english_to_french('We'), 'Nous') 
    def test3(self):
         self.assertEqual(english_to_french('Hello'), 'Bonjour') 
unittest.main()