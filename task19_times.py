#Displays the times table for numbers from 1-12    

import tkinter as tk

def table():
    entered = int(number.get())
    output = ""
    for i in range(1, 13):
            output = output + f"{i} x {entered} = {i * entered}\n"
            answer.config(text=output)

window = tk.Tk()
window.title("Custom Times Table")
window.geometry("360x320")

tk.Label(window, text = "Enter a Number: ").pack(pady=5)
number = tk.Entry(window)
number.pack()

tk.Button(window, text = "Show Times Table", command = table).pack(pady=15)
answer = tk.Label(window, text = "")
answer.pack()

window.mainloop()