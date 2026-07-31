import nltk
from nltk import PCFG
from nltk.parse import ViterbiParser

grammar = PCFG.fromstring("""
S -> NP VP [1.0]
NP -> Det N [0.7] | 'John' [0.3]
VP -> V [0.5] | V NP [0.5]
Det -> 'the' [1.0]
N -> 'girl' [0.5] | 'apple' [0.5]
V -> 'runs' [0.5] | 'eats' [0.5]
""")

parser = ViterbiParser(grammar)

sentence = input("Enter sentence: ").split()

for tree in parser.parse(sentence):
    print(tree)
    print("Probability:", tree.prob())
