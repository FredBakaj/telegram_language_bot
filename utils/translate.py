from googletrans import Translator
from langdetect import detect
from iso639 import languages



def translate_text(text, target) -> str:
    translator = Translator()

    translated_text = translator.translate(text, dest=target)
    return translated_text.text


def detect_text_language(text) -> str:
    lang = detect(text)
    return lang


if __name__ == '__main__':
    result = detect_text_language("Print the result")
    print(result)
    result = translate_text("Print the result", "uk")
    print(result)
