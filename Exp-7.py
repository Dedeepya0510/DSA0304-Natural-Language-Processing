import nltk

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger_eng')

text = "The cat is sleeping"

tokens = nltk.word_tokenize(text)

print(nltk.pos_tag(tokens))
