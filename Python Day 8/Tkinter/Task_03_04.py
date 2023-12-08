import tkinter as tk
from tkinter import *
"""
x1 = 300 -> 300
y1 = 150 -> 150
x2 = 400 -> 400
y2 = 250 -> 50
"""
def AnimeArm():
    global y2, direction
    if(y2 >= 250):
        direction = -5
    elif(y2 <= 50):
        direction = 5

    y2 += direction

    canvas.delete("rightArm")
    canvas.create_line(300, 150, 400, y2, fill="orange", width=3, tags="rightArm")
    canvas.after(10, AnimeArm)


root = tk.Tk()
root.title("Stickman")
root.geometry("600x600")

canvas = tk.Canvas(root, width=600, height=600)
canvas.pack()

y2 = 250
direction = -5
#Body
canvas.create_line(300, 120, 300, 350, fill="red", width=3)

#Legs
canvas.create_line(300, 350, 400, 450, fill="blue", width=3)
canvas.create_line(300, 350, 200, 450, fill="green", width=3)

#Arms
canvas.create_line(300, 150, 400, y2, fill="orange", tags="rightArm", width=3) # => Anime Arm
canvas.create_line(300, 150, 200, 250, fill="purple", width=3)

#Head
canvas.create_oval(280, 80, 320, 120, fill="cyan", outline="cyan")

AnimeArm()
root.mainloop()