import nltk
from nltk import CFG
from nltk.parse import EarleyChartParser

grammar = CFG.fromstring("""
S -> NP VP
NP -> Det N
VP -> V
Det -> 'a'
N -> 'dog'
V -> 'runs'
""")

parser = EarleyChartParser(grammar)

sentence = input("Enter sentence: ").split()

found = False
for tree in parser.parse(sentence):
    print(tree)
    found = True

if not found:
    print("Invalid Sentence")
