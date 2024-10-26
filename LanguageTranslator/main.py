from googletrans import Translator


def translate_text(text, src_lang, dest_lang):
    """
    Translates the given text from the source language to the destination language.
    Uses the Google Translate API.

    Args:
            text (str): The text to be translated.
            src_lang (str): The source language code.
            dest_lang (str): The destination language code.

    Returns:
            str: The translated text.
    """
    translator = Translator()
    try:
        translated = translator.translate(text, src=src_lang, dest=dest_lang)
        return translated.text
    except Exception as e:
        return f"An error occurred: {e}"


if __name__ == "__main__":
    text_to_translate = input(
        "Enter the text to translate from english to spanish: ")
    source_language = "en"  # English
    destination_language = "es"  # Spanish

    translated_text = translate_text(
        text_to_translate, source_language, destination_language)
    print(f"Translated text: {translated_text}")
