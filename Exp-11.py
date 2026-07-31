import nltk
from nltk import CFG
from nltk.parse import RecursiveDescentParser

grammar = CFG.fromstring("""
S -> NP VP
NP -> Det N
VP -> V NP
Det -> 'the'
N -> 'boy' | 'apple'
V -> 'eats'
""")

parser = RecursiveDescentParser(grammar)

sentence = input("Enter sentence: ").split()

found = False
for tree in parser.parse(sentence):
    print(tree)
    found = True

if not found:
    print("Sentence not accepted")
