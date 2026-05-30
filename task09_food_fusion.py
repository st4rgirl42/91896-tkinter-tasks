# Ask the user for their favourite food display it on a label
import tkinter as tk

def combine():
    Food1 = food1.get()
    Food2 = food2.get()
    output_label.config(text=f" {Food1}{Food2}")

window = tk.Tk()  
window.title("Food Fusion")
window.geometry("360x180")

tk.Label(window, text="Favourite food 1").pack(pady=5)
food1 = tk.Entry(window)
food1.pack()

tk.Label(window, text="Favourite food 2").pack(pady=5)
food2 = tk.Entry(window)
food2.pack()

tk.Button(window, text="Combine", command=combine).pack(pady=10)
output_label = tk.Label(window, text="")
output_label.pack()

window.mainloop()