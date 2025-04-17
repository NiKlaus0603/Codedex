from translate import Translator
translator= Translator(to_lang="es")

# English text  translation to Spanish, French, and German  text translation
text = 'Hello, how are you?'

translation = translator.translate(text)
print('Spanish Translation:', translation)