import random

words = input("Enter sentence: ").split()

tags = ["NN", "VB", "JJ"]

for word in words:
    print(word, "->", random.choice(tags))
