#Password Checker GUI

import tkinter as tk

def check_password():
    entered = password_box.get()
    if entered == "eggs2026": 
        status.config(text = "Access Granted", fg = "green")
    else:
        status.config(text = "Access Denied", fg = "red")

window = tk.Tk()
window.title("EGGS Login")
window.geometry("360x150")

tk.Label(window, text = "Password: ").pack()
password_box = tk.Entry(window, show = "*")
password_box.pack()

tk.Button(window, text = "Log In", command = check_password).pack(pady=5)
status = tk.Label(window, text = "")
status.pack()

window.mainloop()