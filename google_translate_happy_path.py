
# Code is based on this tutorial about how to run Google Translate using API
# https://codelabs.developers.google.com/codelabs/cloud-translation-python3#0

# All you need to do is run the tutorial setup before running this script with Google Cloud Shell.


from os import environ

from google.cloud import translate

sample_text = "Hello world!"
target_languages = {"en":"Hello world!",
                    "es":"¡Hola Mundo!",
                    "hi":"हैलो वर्ल्ड!",
                    "zh":"你好，世界！",
                    "fr":"Bonjour le monde!",
                    "ar":"مرحبا بالعالم!",
                    "bn":"ওহে বিশ্ব!",
                    "ru":"Привет, мир!",
                    "pt":"Olá Mundo!",
                    "da":"Hej Verden!",
                    "eu":"Kaixo Mundua!"}


project_id = environ.get("PROJECT_ID", "")
assert project_id
parent = f"projects/{project_id}"
client = translate.TranslationServiceClient()
language_key = list(target_languages.keys())


for n in language_key:
    target_language_code = n
    expected_translation = target_languages.get(target_language_code)

    response = client.translate_text(
        contents=[sample_text],
        target_language_code=target_language_code,
        parent=parent,
    )

    for translation in response.translations:
        assert translation.translated_text == expected_translation, \
        "FAIL: (" + str(target_language_code) + "), Found: " + str(translation.translated_text) + ", Expected: " + str(expected_translation)
