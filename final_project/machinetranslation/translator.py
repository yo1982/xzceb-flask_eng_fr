import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

language_translator.set_disable_ssl_verification(True)


def english_to_french(english_text):
    french_text=language_translator.translate(
    text=english_text,
    model_id='en-fr').get_result()#get the translation
    french_text=french_text["translations"][0]['translation']#Extract the text from the dictionary
    return french_text

def french_to_english(french_text):
    'write the code here'
    english_text=language_translator.translate(
    text=french_text,
    model_id='fr-en').get_result()
    english_text=english_text["translations"][0]['translation']#Extract the text from the dictionary
    return english_text