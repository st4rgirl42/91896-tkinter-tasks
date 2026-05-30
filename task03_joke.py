#joke.py
#Displays a joke in a tkinter window
#Author: Laaibah    Date: 19th May, 2026

import tkinter as tk

window = tk.Tk()
window.title("Joke Time")
window.geometry("400x150")

joke = tk.Label(window, text="Me and my friends started a aband called 999 megabytes")
punchline = tk.Label(window, text="We still don't have a gig though")
joke.pack(pady=10)
punchline.pack()

window.mainloop()