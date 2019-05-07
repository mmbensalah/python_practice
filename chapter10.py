
def translate(text):
    pirate_dict = {"man":"matey", "is":"be"}
    words = text.split(" ")

    new_sentence = []
    for i, word in enumerate(words):
        if word in pirate_dict:
            new_sentence.append(pirate_dict[word])
    return " ".join(new_sentence)

def testEqual(actual, expected):
    return actual == expected

print(testEqual(translate("man is"), "matey be"))
