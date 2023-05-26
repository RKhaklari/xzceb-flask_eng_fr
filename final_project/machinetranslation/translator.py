''' translator code '''
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

authenticator = IAMAuthenticator('{apikey}')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator)
load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

def english_to_french(english_text):
    """ translates english to french """
    french_text = language_translator.translate(
        text=english_text, model_id='en_fr'
    ).get_result()
    return french_text

def french_to_english(french_text):
    """ translates french to english """
    english_text = language_translator.translate(
        text=french_text, model_id='fr_en'
    ).get_result()
    return english_text
