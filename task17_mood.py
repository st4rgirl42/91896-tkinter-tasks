#Mood randomiser

import tkinter as tk
import random

def random_mood():
    number = random.randint(1,3)
    if number == 1: 
        mood.config(text = "☺ Happy", fg = "goldenrod", font=18)
    elif number == 2:
        mood.config(text = "— Neutral", fg = "purple", font=18)
    elif number == 3:
        mood.config(text = "☹ Sad", fg = "blue", font=18)


window = tk.Tk()
window.title("Mood Randomiser")
window.geometry("360x120")

tk.Button(window, text = "Roll My Mood", font=20, command = random_mood,).pack(pady=25)
mood = tk.Label(window, text = "")
mood.pack()

window.mainloop()