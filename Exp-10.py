words=["I","am","playing","football"]

for word in words:
    tag="NN"

    if word.endswith("ing"):
        tag="VBG"

    print(word,"->",tag)
