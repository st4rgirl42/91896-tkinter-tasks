import tkinter as tk

items = ["Nutella", "Bread", "Mushrooms", "Cheese"]

def add():
    new_item = item.get()
    shopping_list.insert(tk.END, new_item)

def clear():
    shopping_list.delete(0, tk.END)


window = tk.Tk()
window.title("Shopping List")
window.geometry("360x280") 

shopping_list = tk.Listbox(window, height=8, width=20)
for food in items:
    shopping_list.insert(tk.END, food)
shopping_list.pack(pady=10)   

tk.Label(window, text = "Enter your Item: ").pack()
item = tk.Entry(window)
item.pack()

tk.Button(window, text = "Add", command = add).pack(pady=5)

tk.Button(window, text = "Clear All", command = clear).pack(pady=5)


window.mainloop()