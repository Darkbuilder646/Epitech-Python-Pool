import tkinter as ctk
import random as rd
#import HangmanGUI as GUIgame

class HangmanGame:
    def __init__(self):
        with open("Hangman Game v2.0\FrenchWord.txt") as file:
            self.lines = file.readlines()
        #self.wordToGuess = rd.choice(self.lines).lower()
        self.wordToGuess = "pizza"  # //! Pour le débogage et les tests
        self.bestAttempts = 1000
        self.hideword = "_" * len(self.wordToGuess)
        self.finishGame = False

    def get_hideword(self):
        return self.hideword

    def draw_hangman(self, index: int): #//* Faire apparaitre sur la frame principal sur ctk
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
        pass

    def game_logic(self,): #//* Changer la logi => sans de while => appelle via les lettre button
        hideWord = "_" * len(self.wordToGuess)
        letterUsed = []
        error = 0
        attempts = 0

        while error < 10 or not self.finishGame:
            #print("Word to find :", hideWord, "\nNumber of error :", error, " Number of attempts :", attempts, "\nLetter used :", letterUsed)
            playerGuess = input("Enter a letter or a word ").lower()

            if(len(playerGuess) > 1): #//? Si c'est un mot
                if(playerGuess == self.wordToGuess):
                    self.finishGame = True  
                    break
                else:
                    print("It not that word")
                    error += 1
                    attempts +=1
                    hangman_game.draw_hangman(error)

            elif(playerGuess not in self.wordToGuess): #//? Si la lettre n'est pas dans le mot
                print("There is no", playerGuess, "in the word")
                letterUsed.append(playerGuess)
                error += 1
                attempts += 1
                hangman_game.draw_hangman(error)

            else:
                for index, char in enumerate(self.wordToGuess): #//? La lettre est dans le mot
                    if char == playerGuess:
                        hideWord = hideWord[:index] + playerGuess + hideWord[index+1:]

            if(playerGuess not in letterUsed): #//? double lettre check
                letterUsed.append(playerGuess)
            attempts += 1
            hangman_game.draw_hangman(error)

            if("_" not in hideWord):
                self.finishGame = True
                break
        
        if self.finishGame:
            if attempts <= self.bestAttempts:
                print("Best ever !!! \nYou're guessed", self.wordToGuess, "in", attempts, "attempts.\n")
                self.bestAttempts = attempts
            else:
                print("You're guessed", self.wordToGuess, "in", attempts, "attempts.\n The record is", self.bestAttempts, "attempts.\n")

        if(error >= 10):
            print("You lose the game\nThe word was", self.wordToGuess)
            pass

    def start_game(self):
        self.finishGame = False
        #self.game_logic()
        #GUIgame.LaunchGUI()

if __name__ == "__main__":
    hangman_game = HangmanGame()
    hangman_game.start_game()
    """
    while True:
        choice = input("Do you want to play the hangman game? Choose 'yes' or 'no': ")
        if choice == "yes":
            hangman_game.start_game()
        elif choice == "no":
            quit()
        else:
            print("Invalid input")
    """