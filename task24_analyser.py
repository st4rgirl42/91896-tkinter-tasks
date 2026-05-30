import tkinter as tk

def analyse():
    message = text.get()
    length.config(text = f"Your message has {len(message)} characters.")
    if "e" in message:
        letter_e.config(text = f"The letter ‘e’ IS in your message")
    else:
        letter_e.config(text = f"The letter ‘e’ IS NOT in your message")

window = tk.Tk()
window.title("Length Analyser")
window.geometry("360x220") 

tk.Label(window, text = "Enter a Message: ").pack(pady=15)
text = tk.Entry(window)
text.pack()

tk.Button(window, text = "Analyse", command = analyse).pack(pady=20)

length = tk.Label(window, text = "")
length.pack()

letter_e = tk.Label(window, text = "")
letter_e.pack()

window.mainloop()