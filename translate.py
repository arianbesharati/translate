from deep_translator import GoogleTranslator
def translator():
    text =  input("Enter your text: ")
    print("""supported languages:
    arabic: ar
    armenian: hy
    azerbaijani: az
    english: en
    french: fr
    german: de
    italian: it
    japanse: jw
    persian: fa
    russian: ru
    turkish: tr""")
    target = input("Enter your target language: ")
    translated = GoogleTranslator(source='auto',target= target).translate(text)
    print("translated text: ", translated)



translator()