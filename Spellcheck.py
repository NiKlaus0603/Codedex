from textblob import TextBlob
text = 'I love programing!'
blob = TextBlob(text)
corrected_text = blob.correct()

print('original text:', text)
print('corrected text:', corrected_text)