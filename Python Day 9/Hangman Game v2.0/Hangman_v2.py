import random as rd

gameLaunch = True
finishGame = False
bestAttempts = 1000

with open("Hangman Game v2.0\FrenchWord.txt") as file:
    lines = file.readlines()

#wordToGuess = rd.choice(lines).lower()
wordToGuess = "pizza" #//! Pour le debug et test
hideWord = "_" * len(wordToGuess)

def DrawHangman(index: int):
    pics = ["\n=========",
            
            "\n      |\n      |\n      |\n      |\n      |\n=========",

            "\n     \|\n      |\n      |\n      |\n      |\n=========",

            "\n  +---+\n     \|\n      |\n      |\n      |\n      |\n=========",

            "\n  +---+\n  |  \|\n      |\n      |\n      |\n      |\n=========", 

            "\n  +---+\n  |  \|\n  O   |\n      |\n      |\n      |\n=========",

            "\n  +---+\n  |  \|\n  O   |\n  |   |\n      |\n      |\n=========",

            "\n  +---+\n  |  \|\n  O   |\n /|   |\n      |\n      |\n=========", 

            "\n  +---+\n  |  \|\n  O   |\n /|\  |\n      |\n      |\n=========",

            "\n  +---+\n  |  \|\n  O   |\n /|\  |\n /    |\n      |\n=========",

            "\n  +---+\n  |  \|\n  O   |\n /|\  |\n / \  |\n      |\n========="] 
    print(pics[index])

def GameLogique(wordToGuess: str):
    global bestAttempts, hideWord
    hideWord = "_" * len(wordToGuess)
    letterUsed = []
    error = 0
    attempts = 0
    DrawHangman(error)

    while error < 10 or not finishGame:
        print("Word to find :", hideWord, "\nNumber of error :", error, " Number of attempts :", attempts, "\nLetter used :", letterUsed)
        
        playerGuess = input("Enter a letter or a word ").lower()

        if(len(playerGuess) > 1): #//? Si c'est un mot
            if(playerGuess == wordToGuess):
                finishGame = True  
                break
            else:
                print("It not that word")
                error += 1
                attempts +=1
                DrawHangman(error)

        elif(playerGuess not in wordToGuess): #//? Si la lettre n'est pas dans le mot
            print("There is no", playerGuess, "in the word")
            letterUsed.append(playerGuess)
            error += 1
            attempts += 1
            DrawHangman(error)

        else:
            for index, char in enumerate(wordToGuess): #//? La lettre est dans le mot
                if char == playerGuess:
                    hideWord = hideWord[:index] + playerGuess + hideWord[index+1:]

        if(playerGuess not in letterUsed): #//? double lettre check
            letterUsed.append(playerGuess)
        attempts += 1
        DrawHangman(error)

        if("_" not in hideWord):
            finishGame = True
            break

    if finishGame:
        if attempts <= bestAttempts:
            print("Best ever !!! \nYou're guessed", wordToGuess, "in", attempts, "attempts.\n")
            bestAttempts = attempts
        else:
            print("You're guessed", wordToGuess, "in", attempts, "attempts.\n The record is", bestAttempts,
                  "attempts.\n")

    if(error >= 10):
        print("You lose the game\nThe word was", wordToGuess)  

while True:
    choice = input("Do you want to play at the hangman game ? \nChoose 'yes' or 'no' ")
    if(choice == "yes"):
        finishGame = False
        GameLogique(wordToGuess)
    elif(choice == "no"):
        quit()
    else:
        print("It not a answer")
