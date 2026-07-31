import re

words = ["playing","played","beautiful","dog"]

for word in words:
    if re.search("ing$", word):
        print(word,"-> Verb")
    elif re.search("ed$", word):
        print(word,"-> Past Verb")
    elif re.search("ful$", word):
        print(word,"-> Adjective")
    else:
        print(word,"-> Noun")
