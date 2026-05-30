#Guess the number

import tkinter as tk

def check_number():
    entered = int(number.get())
    if entered == 5: 
        status.config(text = "You guessed correctly!")
    elif entered > 5:
        status.config(text = "Too high")
    elif entered < 5:
        status.config(text = "Too low")

window = tk.Tk()
window.title("Guess the Secret Number")
window.geometry("360x150")

tk.Label(window, text = "Guess a Number: ").pack()
number = tk.Entry(window)
number.pack()

tk.Button(window, text = "Guess", command = check_number).pack(pady=5)
status = tk.Label(window, text = "")
status.pack()

window.mainloop()