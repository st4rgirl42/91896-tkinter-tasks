# Ask the user for their name and town and display it on a label
import tkinter as tk

def greet():
    name = name_box.get()
    town = town_box.get()
    output_label.config(text=f"Hello {name}, I hope the weather is good in {town}.")

window = tk.Tk()
window.title("Personal Greeter")
window.geometry("360x180")

tk.Label(window, text="What is your name?").pack(pady=5)
name_box = tk.Entry(window)
name_box.pack()

tk.Label(window, text="What town do you live in?").pack(pady=5)
town_box = tk.Entry(window)
town_box.pack()

tk.Button(window, text="Greet me", command=greet).pack(pady=10)
output_label = tk.Label(window, text="")
output_label.pack()

window.mainloop()