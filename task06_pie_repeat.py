#pie_repeat.py
#Repeats the line "I want a pie for lunch" ten times in a tkinter window
#Author: Laaibah    Date: 20th May, 2026

import tkinter as tk

window = tk.Tk() 
window.title("Lunch")
window.geometry("400x280")

for i in range(10):
    tk.Label(window, text="I want a pie for lunch", font=("Times New Roman", 14)).pack()

window.mainloop() 