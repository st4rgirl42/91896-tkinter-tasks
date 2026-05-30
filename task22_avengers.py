import tkinter as tk

avengers = ["Captain America", "Thor", "The Hulk", "Iron Man"]

def special():
    hammer.config(text = f"The character who has a special hammer is {avengers[1]}")


window = tk.Tk()
window.title("Avengers")
window.geometry("360x200") 

hero_box = tk.Listbox(window, height=5, width=25)
for hero in avengers:
    hero_box.insert(tk.END, hero)
hero_box.pack(pady=10)   

tk.Button(window, text = "Special Hammer", command = special).pack(pady=5)
hammer = tk.Label(window, text = "")
hammer.pack()


window.mainloop()
