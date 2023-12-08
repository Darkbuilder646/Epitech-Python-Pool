import random as rd

with open("Hangman Game\FrenchWord.txt") as file:
    lines = file.readlines()

wordToGuess = rd.choice(lines).lower()

def DrawHangman(index: int):
    pics = ["  +---+\n  |   |\n      |\n      |\n      |\n      |\n=========", 

        "  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n=========",

        "  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n=========",

        "  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n=========", 

        "  +---+\n  |   |\n  O   |\n /|\  |\n      |\n      |\n=========",

        "  +---+\n  |   |\n  O   |\n /|\  |\n /    |\n      |\n=========",

        "  +---+\n  |   |\n  O   |\n /|\  |\n / \  |\n      |\n========="] 
    print(pics[index])

def GameLogique(wordToGuess: str):
    hideWord = "_" * len(wordToGuess)
    letterUsed = []
    error = 0
    DrawHangman(error)

    while error < 6:
        print("Word to find :", hideWord, "\nNumber of error :", error, "\nLetter used :", letterUsed)
        playerGuess = input("Enter a letter or a word ").lower()
        print("\n")

        if(len(playerGuess) > 1):
            if(playerGuess == wordToGuess):
                print("You win ! \nYou found the word :", wordToGuess)
                quit()
            else:
                print("It not that word")
                error += 1
                DrawHangman(error)
                continue

        if(playerGuess not in wordToGuess):
            print("There is no", playerGuess, "in the word")
            letterUsed.append(playerGuess)
            error += 1
            DrawHangman(error)
            continue

        for index, char in enumerate(wordToGuess):
            if char == playerGuess:
                hideWord = hideWord[:index] + playerGuess + hideWord[index+1:]

        letterUsed.append(playerGuess)
        DrawHangman(error)
        

    print("You lose the game\nThe word was", wordToGuess)         

GameLogique(wordToGuess)
