#royals.py
#Displays a the lyrics to the song 'Royal' in a tkinter window
#Author: Laaibah    Date: 20th May, 2026

import tkinter as tk

window = tk.Tk() 
window.title("Royals")
window.geometry("400x150")

line5 = tk.Label(window, text="Royals", font=("Times New Roman", 18, "bold"))
line1 = tk.Label(window, text="I've never seen a diamond in the flesh", font=("Times New Roman", 14))
line2 = tk.Label(window, text="I cut my teeth on wedding rings, in the movies", font=("Times New Roman", 14))
line3 = tk.Label(window, text="And I'm not proud of my address", font=("Times New Roman", 14))
line4 = tk.Label(window, text="In a torn up town, no post code envy", font=("Times New Roman", 14))
line5.pack()
line1.pack()
line2.pack()
line3.pack()
line4.pack()


window.mainloop() 