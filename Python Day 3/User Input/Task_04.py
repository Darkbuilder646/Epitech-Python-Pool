#Extract the first word of sentence
#And join them in one sentence
#//? En plus demander à l'user combien de sentence
#//? faire une boucle d'input

def TakeFirstWord(listOfWord: list, sentence: str):
    test = sentence.split(" ")
    listOfWord.append(test[0])

firstWordList = []
nbrInput = int(input("How many sentence ?\n"))

for i in range(nbrInput):
    sentence = str(input("Write a sentence\n"))
    TakeFirstWord(firstWordList, sentence)

finalString = " ".join(firstWordList)
print (finalString)
