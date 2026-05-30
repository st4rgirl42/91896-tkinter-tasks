#quote.py
#Displays a quote in a tkinter window
#Author: Laaibah    Date: 20th May, 2026

import tkinter as tk

window = tk.Tk()
window.title("My favourtie quote")
window.geometry("500x150")

quote = tk.Label(window, text="I am a mosaic of everyone I have ever loved, even for a heartbeat", font=("Times New Roman", 14))
credit = tk.Label(window, text="~Hannah Hassler", font=("Times New Roman", 12, "italic"))
quote.pack(pady=10)
credit.pack()

window.mainloop()