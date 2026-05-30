# Tip Calculator helping customers with a 15% or 20% tip 

import tkinter as tk

def calculate():
    price = float(cost.get()) 
    Gst = float(f"{15/100 * price :.2f}")
    total.config(text= f"Total cost: ${Gst + price + 1450 :.2f}")

window = tk.Tk()  
window.title("Car Salesperson")
window.geometry("610x160")

tk.Label(window, text="Enter the base price of your car:", font= ("Times New Roman",12, "bold")).pack(pady=5)
tk.Label(window, text="Total includes: 15% GST and set fees; $120 licence plates, $450 tow bar, $680 sound system, $200 seat covers", font=("Times New Roman", 10, "italic")).pack(pady=5)
cost = tk.Entry(window)
cost.pack()

tk.Button(window, text="Calculate Total", command=calculate).pack(pady=10)
total = tk.Label(window, text="")
total.pack()



window.mainloop()