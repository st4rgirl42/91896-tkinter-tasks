# GST Calculator 

import tkinter as tk

def calculate():
    price = float(cost.get()) 
    Gst = float(f"{15/100 * price :.2f}")
    gst.config(text= f"GST Amount: ${15/100 * price :.2f}")
    total.config(text= f"Total Price: ${price + Gst }")

window = tk.Tk()  
window.title("GST Calculator")
window.geometry("360x150")

tk.Label(window, text="Enter a price (excluding GST):").pack(pady=5)
cost = tk.Entry(window)
cost.pack()

tk.Button(window, text="Calculate GST price", command=calculate).pack(pady=10)
gst = tk.Label(window, text="")
gst.pack()

total = tk.Label(window, text="")
total.pack()


window.mainloop()