# Tip Calculator helping customers with a 15% or 20% tip 

import tkinter as tk

def calculate():
    price = float(cost.get()) 
    tip1.config(text= f"15% Tip: ${15/100 * price :.2f}")
    tip2.config(text= f"20% Tip: ${20/100 * price :.2f}")

window = tk.Tk()  
window.title("Tip Calculator")
window.geometry("360x150")

tk.Label(window, text="Enter a your restaurant bill total:").pack(pady=5)
cost = tk.Entry(window)
cost.pack()

tk.Button(window, text="Calculate Tip Amount", command=calculate).pack(pady=10)
tip1 = tk.Label(window, text="")
tip1.pack()

tip2 = tk.Label(window, text="")
tip2.pack()


window.mainloop()