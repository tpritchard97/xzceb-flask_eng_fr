import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
Translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

def englishToFrench(englishText):
    "Hello World"
    return frenchText

#def frenchToEnglish(frenchText):
    #"Bonjour"
    #return englishText