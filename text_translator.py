import requests

def translate_text(text, source_language, target_language):
    try:
        url = f"https://translate.googleapis.com/translate_a/single?client=gtx&sl={source_language}&tl={target_language}&dt=t&q={text}"
        response = requests.get(url)
        json_data = response.json()
        translated_text = json_data[0][0][0]
        return translated_text
    except Exception as e:
        print("Error while translating text:", str(e))
        return None

def main():
    text = input("Enter the text to be translated: ")
    source_language = input("Enter the source language code: ")
    target_language = input("Enter the target language code: ")
    translated_text = translate_text(text, source_language, target_language)
    if translated_text:
        print("Translated text:", translated_text)

if __name__ == "__main__":
    main()
