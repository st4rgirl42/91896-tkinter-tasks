#hello_world.py
#Displays a friendly greeting in a tkinter window
#Author: Laaibah    Date: 19th May, 2026



import tkinter as tk

window = tk.Tk()
window.title("Hello World")
window.geometry("320x120")

greeting = tk.Label(window, text="Hello World!", font=("Times New Roman", 18))
greeting.pack(pady=50)

window.mainloop()

# Ask the user for their name and display it on a label
import tkinter as tk

def greet():
    name = name_box.get()
    output_label.config(text=f"Kia ora, {name}!")

window = tk.Tk()
window.title("Personal Greeter")
window.geometry("360x180")

tk.Label(window, text="What is your name?").pack(pady=5)
name_box = tk.Entry(window)
name_box.pack()

tk.Button(window, text="Greet me", command=greet).pack(pady=10)
output_label = tk.Label(window, text="")
output_label.pack()

window.mainloop()
