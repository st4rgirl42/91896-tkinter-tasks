#Count down 

import tkinter as tk

def table():
    output = ""
    for i in range(10, 0, -1):
        output = output + f"{i}\n"
        number.config(text=output)
                 
    output = output + "Blast off!"
    number.config(text=output)

window = tk.Tk()
window.title("Countdown Timer")
window.geometry("360x280")

tk.Button(window, text = "Countdown", command = table).pack(pady=25)
number = tk.Label(window, text = "")
number.pack()

window.mainloop()