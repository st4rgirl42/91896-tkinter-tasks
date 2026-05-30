#Displays the Hello World as many times as wanted

import tkinter as tk

def table():
    count = int(number.get())
    for i in range(count):
        tk.Label(window, text="Hello World").pack()

window = tk.Tk()
window.title("Custom Times Table")
window.geometry("360x320")

tk.Label(window, text = "Enter a Number: ").pack()
number = tk.Entry(window)
number.pack()

tk.Button(window, text = "Hello World :)", command = table).pack(pady=5)
answer = tk.Label(window, text = "")
answer.pack()

window.mainloop()