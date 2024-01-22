from components.ember import Ember
from components.emberosaurus import Emberosaurus

ember = Ember()
emberosaurus = Emberosaurus(ember)

while True:
    sentence = input("Input a sentence: ")
    word = input("Input a word: ")
    print("")
    ranked = emberosaurus.ranked_synonyms(sentence, word)
    for synonym, score in ranked:
        print(f"{synonym} ({score:.3f})")
