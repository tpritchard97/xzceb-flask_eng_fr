import unittest
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from translator import english_to_french, french_to_english

apikey = 'kkaFAgA62ZHKfEVm1OICOGv6GSbgoBS6kpztZdjYP2u5'
url = 'https://api.us-east.language-translator.watson.cloud.ibm.com/instances/42d76f9a-3490-4f89-8477-f927cb768cde'

authenticator = IAMAuthenticator(apikey)
translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)
translator.set_service_url(url)

class TranslatorTestCase(unittest.TestCase):
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
    unittest.main(verbosity=2)
