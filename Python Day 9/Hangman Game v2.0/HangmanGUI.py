import customtkinter as ctk
import Hangman_v3 as hmGame

hangman_game = hmGame.HangmanGame()

root = ctk.CTk()
root.geometry("800x600")
root.title("Hangman Game")

def ClickButton(letter):
    print(f"Bouton {letter}")

def updateLabel():
    newHideword = hangman_game.get_hideword()
    hideWordText.set(newHideword)


hideWordText = ctk.StringVar()
hideWordText.set(hangman_game.get_hideword())

#---- Création de l'UI ----
hangmanFrame = ctk.CTkFrame(root,width=600, height=350, border_width=3)
hangmanFrame.pack(pady=10)

hideWordLabel = ctk.CTkLabel(hangmanFrame, text=hideWordText)
hideWordLabel.pack(side=ctk.TOP, pady="5 50", padx=50)

letterFrame = ctk.CTkFrame(root, width=700, height=300)
letterFrame.pack(pady=20)

frame1 = ctk.CTkFrame(letterFrame, width=700, height=75)
frame1.pack()

frame2 = ctk.CTkFrame(letterFrame, width=700, height=75)
frame2.pack()

frame3 = ctk.CTkFrame(letterFrame, width=700, height=75)
frame3.pack()

letters = [chr(i) for i in range(65, 91)]

rowCount = [8,10,8]
frames = [frame1, frame2, frame3]

for i, count in enumerate(rowCount):
    for j in range(count):
        if(letters):
            letter = letters.pop(0)
            button = ctk.CTkButton(frames[i], text=letter, command=lambda l=letter: hangman_game.game_logic(l), width=50, height=50)
            button.grid(row=0, column=j, pady="5", padx="5")

def LaunchGUI():
    root.mainloop()