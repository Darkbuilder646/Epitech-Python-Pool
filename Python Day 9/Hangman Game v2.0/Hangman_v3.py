import random as rd
import HangmanGUI as GUIgame

class HangmanGame:
    def __init__(self):
        with open("Hangman Game v2.0\FrenchWord.txt") as file:
            self.lines = file.readlines()
        #self.wordToGuess = rd.choice(self.lines).lower()
        self.wordToGuess = "pizza"  # //! Pour le débogage et les tests
        self.bestAttempts = 1000
        self.hideWord = "_" * len(self.wordToGuess)
        self.finishGame = False

    def get_hideword(self):
        return self.hideWord

    def draw_hangman(self, index: int): #//TODO Faire apparaitre sur la frame principal sur ctk
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

    def game_logic(self, letter: str): #//TODO Changer la logi => sans de while => appelle via les lettre button
        letterUsed = []
        error = 0
        attempts = 0

        if error < 10 or not self.finishGame:
            letter = letter.lower()

            if(letter not in self.wordToGuess): #//? Si la lettre n'est pas dans le mot
                print("There is no", letter, "in the word")
                letterUsed.append(letter)
                error += 1
                attempts += 1
                #//*hangman_game.draw_hangman(error)

            else:
                for index, char in enumerate(self.wordToGuess): #//? La lettre est dans le mot
                    if char == letter:
                        self.hideWord = self.hideWord[:index] + letter + self.hideWord[index+1:]
                        GUIgame.updateLabel()

            if(letter not in letterUsed): #//? double lettre check
                letterUsed.append(letter)
            attempts += 1
            #//*hangman_game.draw_hangman(error)

            if("_" not in self.hideWord):
                self.finishGame = True
        
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
        GUIgame.LaunchGUI()

if __name__ == "__main__":
    hangman_game = HangmanGame()
    hangman_game.start_game()
