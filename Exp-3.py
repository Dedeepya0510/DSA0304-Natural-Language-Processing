from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

word = "running"

print("Original Word:", word)
print("Base Form:", lemmatizer.lemmatize(word, pos='v'))
