import nltk
from nltk.stem import PorterStemmer

stemmer = PorterStemmer()

words = ["running", "playing", "studies", "happiness", "walking"]

print("Original\tStem")

for word in words:
    print(word, "\t", stemmer.stem(word))
