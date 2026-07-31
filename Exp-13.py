import nltk
from nltk import CFG
from nltk.parse import ChartParser

grammar = CFG.fromstring("""
S -> NP VP
NP -> Det N
VP -> V
Det -> 'the'
N -> 'cat'
V -> 'sleeps'
""")

parser = ChartParser(grammar)

sentence = input("Enter sentence: ").split()

for tree in parser.parse(sentence):
    print(tree)
