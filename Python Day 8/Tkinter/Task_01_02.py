import tkinter as tk
from tkinter import *
root = tk.Tk()
root.title("Test for Tkinter")

root.geometry("350x500")
root.grid_rowconfigure(0, weight=1)


def PrintToTerminal():
    texte = inputField.get()
    print(texte)

labelFrm = tk.LabelFrame(root, text="This is a label",bd=3)
labelFrm.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

inputField = tk.Entry(labelFrm)
inputField.grid(row=0, column=0, pady="10 10", padx="10 20")

button = tk.Button(labelFrm, text="Just a button")
button.grid(row=0, column=1, padx="0 10")

button = tk.Button(labelFrm, text="Print Text", command=PrintToTerminal)
button.grid(row=2, column=0)

canvas = tk.Canvas(labelFrm, width=256, height=256, bd=2)
canvas.grid(row=3, column=0)

img = PhotoImage(file="Tkinter\Minecraft_Icon.png")

canvas.create_image(0, 0, anchor=tk.NW, image=img)

root.mainloop()