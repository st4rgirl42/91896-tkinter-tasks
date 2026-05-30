#Helps users calculate their daily calorie intake

import tkinter as tk

daily_limit = 0

food_names = []
calorie_values = []


def set_goal():
    global daily_limit
    goal = goal_entry.get()
    if goal.isdigit():
        daily_limit = int(goal)
        goal_label.config(text = f"Daily Goal: {daily_limit} calories", fg = "green")
        update_total()
    else:
        goal_label.config(text = "Please enter a valid number", fg="red")
        

def update_total():
    total = 0
    for values in calorie_values:
        total += values
    total_calories.config(text = f"Daily Goal: {daily_limit} calories | Current Total: {total} calories")

    if total < daily_limit:
        remaining = daily_limit - total
        limit.config(text = f"You can still eat {remaining} calories today", fg = "green")

    elif total == daily_limit:
        limit.config(text = "You have reached your calorie goal exactly!", fg = "orange")

    else:
        over = total - daily_limit
        limit.config(text = f"You are {over} calories over your limit", fg = "red")


def add():
    food = food_entry.get()
    calories = calories_entry.get()
    if food.strip() == "":
        status_label.config(text = "Error: Food name cannot be blank", fg = "red")
    elif calories.isdigit() == False:
        status_label.config(text = "Error: Calories must be a number", fg = "red")
    elif food in food_names:
        status_label.config(text = "Error: Food already added", fg = "orange")
    else:
        calories = int(calories)
        food_list.insert(tk.END, f"{food}")
        food_names.append(food)
        calorie_values.append(calories)
        status_label.config(text = f"{food} added successfully!", fg = "green")
        food_entry.delete(0, tk.END)
        calories_entry.delete(0, tk.END)
        update_total()

def show(event):
    selected = food_list.curselection()
    if selected:
        index = selected[0]
        food = food_names[index]
        calories = calorie_values[index]
        select.config(text = f"{food} contains {calories} calories", fg = "blue")
        
def delete():
    selected = food_list.curselection()
    if selected:
        index = selected[0]
        food_list.delete(index)
        del food_names[index]
        del calorie_values[index]
        select.config(text = "Food deleted")
        update_total()
    else:
        select.config(text = "Please select a food to delete") 

def clear():
    food_list.delete(0, tk.END)
    food_names.clear()
    calorie_values.clear()
    select.config(text = "All foods removed")
    update_total()



window = tk.Tk()
window.title("Calorie Tracker")
window.geometry("450x620")      

tk.Label(window, text = "Daily Calorie Tracker", font= ("Times New Roman", 18, "bold")).pack(pady=15)     

tk.Label(window, text = "Enter Daily Calorie Goal: ", font= ("Times New Roman", 14 , "bold")).pack()
goal_entry = tk.Entry(window, width=25)
goal_entry.pack(pady=5)
tk.Button(window, text = "Set Goal", command=set_goal).pack()
goal_label = tk.Label(window, text = "")
goal_label.pack()
    
tk.Label(window, text = "Enter a Food: ", font= ("Times New Roman", 12 , "bold")).pack(pady=5)
food_entry = tk.Entry(window, width=25)
food_entry.pack()

tk.Label(window, text = f"Enter Calories : ", font= ("Times New Roman", 12 , "bold")).pack(pady=5)
calories_entry = tk.Entry(window, width=25)
calories_entry.pack()

tk.Button(window, text = "Add Food", command = add).pack(pady=5)
length = tk.Label(window, text = "")
length.pack()

status_label = tk.Label(window, text="Waiting for input...", font=("Times New Roman", 10, "italic"), fg="gray")
status_label.pack()


food_list = tk.Listbox(window, width = 35, height = 7)
food_list.pack()
food_list.bind("<<ListboxSelect>>", show)

total_calories = tk.Label(window, text = "Daily Goal: 0 calories | Current Total: 0 calories", font = ("bold", 10))
total_calories.pack()

limit = tk.Label(window, text = f"You can still eat {daily_limit} calories today", fg = "green")
limit.pack()

select = tk.Label(window, text = "")
select.pack()

tk.Button(window, text = "Delete Selected", command= delete).pack(pady=3)
tk.Button(window, text = "Clear All", command= clear).pack


window.mainloop()