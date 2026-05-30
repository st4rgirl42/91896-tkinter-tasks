# Calculator 


import tkinter as tk

def calculate():
    number1 = int(no1.get()) 
    number2 = int(no2.get())
    answer1.config(text= f"{number1} + {number2} = {number1 + number2}")
    answer2.config(text= f"{number1} - {number2} = {number1 - number2}")
    answer3.config(text= f"{number1} * {number2} = {number1 * number2}")
    answer4.config(text= f"{number1} / {number2} = {number1 / number2}")
    answer5.config(text= f"{number1} % {number2} = {number1 % number2}")

window = tk.Tk()  
window.title("Calculator")
window.geometry("360x260")

tk.Label(window, text="1st Number").pack(pady=5)
no1 = tk.Entry(window)
no1.pack()

tk.Label(window, text="2nd Number").pack(pady=5)
no2 = tk.Entry(window)
no2.pack()

tk.Button(window, text="Calculate", command=calculate).pack(pady=10)


answer1 = tk.Label(window, text="x + y = ?")
answer1.pack()

answer2 = tk.Label(window, text="x - y = ?")
answer2.pack()

answer3 = tk.Label(window, text="x * y = ?")
answer3.pack()

answer4 = tk.Label(window, text="x / y = ?")
answer4.pack()

answer5 = tk.Label(window, text="x % y = ?")
answer5.pack()


window.mainloop()