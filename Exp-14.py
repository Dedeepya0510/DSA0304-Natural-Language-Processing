sentence = input("Enter a sentence: ").split()

rules = {
    "He": "plays",
    "She": "plays",
    "It": "plays",
    "They": "play",
    "We": "play",
    "I": "play"
}

if len(sentence) >= 2:
    subject = sentence[0]
    verb = sentence[1]

    if subject in rules and rules[subject] == verb:
        print("Sentence is Correct")
    else:
        print("Subject-Verb Agreement Error")
else:
    print("Invalid Input")
