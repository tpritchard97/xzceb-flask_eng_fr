import unittest
from translator import english_to_french, french_to_english
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

def test_frenchToEnglish_null_input(self):
        result = french_to_english(None)
        self.assertIsNone(result)

 
def test_englishToFrench_null_input(self):
        result = english_to_french(None)
        self.assertIsNone(result)

def test_frenchToEnglish_translation(self):
        result = french_to_english("Bonjour")
        self.assertEqual(result, "Hello")
        
def test_englishToFrench_translation(self):
        result = english_to_french("Hello")
        self.assertEqual(result, "Bonjour")

if __name__ == '__main__':
    unittest.main()