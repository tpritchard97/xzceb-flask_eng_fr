from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

apikey = "kkaFAgA62ZHKfEVm1OICOGv6GSbgoBS6kpztZdjYP2u5"
url = "https://api.us-east.language-translator.watson.cloud.ibm.com/instances/42d76f9a-3490-4f89-8477-f927cb768cde"

authenticator = IAMAuthenticator(apikey)
translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)
translator.set_service_url(url)

def english_to_french(english_text):
    translation = translator.translate(text=english_text, model_id='en-fr').get_result()
    french_text = translation['translations'][0]['translation']
    return french_text

def french_to_english(french_text):
    translation = translator.translate(text=french_text, model_id='fr-en').get_result()
    english_text = translation['translations'][0]['translation']
    return english_text
