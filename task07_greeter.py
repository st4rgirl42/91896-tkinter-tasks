# Ask the user for their name and display it on a label
import tkinter as tk

def greet():
    name = name_box.get()
    output_label.config(text = "Kia ora, " + name + "!", font="Times New Roman", bg = "purple", fg = "white")

window = tk.Tk()
window.title("Personal Greeter")
window.geometry("360x180")
window.configure(bg = "purple")

tk.Label(window, text="What is your name?", bg = "purple").pack(pady=5)
name_box = tk.Entry(window, foreground = "white")
name_box.pack()

tk.Button(window, text="Greet me", comman=greet, bg = "cyan").pack(pady=10)
output_label = tk.Label(window, text="", bg = "purple")
output_label.pack()


window.mainloop()
