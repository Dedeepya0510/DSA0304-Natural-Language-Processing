import nltk
nltk.download('wordnet')

from nltk.corpus import wordnet

word = input("Enter a word: ")

synsets = wordnet.synsets(word)

if synsets:
    print("Meaning:", synsets[0].definition())
    print("Synonyms:")
    for lemma in synsets[0].lemmas():
        print(lemma.name())
else:
    print("Word not found")
