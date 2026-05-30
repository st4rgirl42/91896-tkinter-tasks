#Password Checker GUI

import tkinter as tk

def check_password():
    entered = password_box.get()
    name = name_box.get()
    if entered == "eggs2026": 
        status.config(text = f"Welcome {name}!", fg = "green")
    else:
        status.config(text = "Try Harder", fg = "red")

window = tk.Tk()
window.title("EGGS Login")
window.geometry("360x150")

tk.Label(window, text = "Your Name: ").pack()
name_box = tk.Entry(window)
name_box.pack()

tk.Label(window, text = "Password: ").pack()
password_box = tk.Entry(window, show = "*")
password_box.pack()

tk.Button(window, text = "Log In", command = check_password).pack(pady=5)
status = tk.Label(window, text = "")
status.pack()

window.mainloop()