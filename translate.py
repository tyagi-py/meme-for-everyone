from googletrans import Translator, LANGUAGES,LANGCODES

translator = Translator()

def translate_text(text, des):
    t = translator.translate(text,dest=des)
    return t.text