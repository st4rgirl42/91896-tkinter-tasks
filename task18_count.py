#Displays every even number from 1-20

import tkinter as tk

def table():
    output = ""
    for i in range(1, 11):
        if i == 10:
            output = output + f"{i*2}"
            number.config(text=output)
        else:
            output = output + f"{i * 2}, "
            number.config(text=output)

window = tk.Tk()
window.title("Counting Label")
window.geometry("360x120")

tk.Button(window, text = "Count to 20", command = table).pack(pady=25)
number = tk.Label(window, text = "")
number.pack()

window.mainloop()