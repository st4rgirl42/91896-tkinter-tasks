#hello.py
#Displays a friendly greeting in a tkinter window
#Author: Laaibah    Date: 19th May, 2026


import tkinter as tk

window = tk.Tk()
window.title("My First App")
window.geometry("400x150")

greeting = tk.Label(window, text="Hello World, nice to meet you.", font=("Arial", 14))
greeting.pack(pady=50)

window.mainloop()