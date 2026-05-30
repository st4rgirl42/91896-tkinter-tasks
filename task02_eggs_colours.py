#eggs_colours.py
#Displays a friendly greeting in a tkinter window in the eggs colours
#Author: Laaibah    Date: 19th May, 2026

import tkinter as tk

window = tk.Tk()
window.title("My First App")
window.geometry("400x150")
window.configure(bg="navy")

greeting = tk.Label(window, text="Hello World, nice to meet you.", font=("Arial", 14), fg="gold", bg="navy")
greeting.pack(pady=50)

window.mainloop()