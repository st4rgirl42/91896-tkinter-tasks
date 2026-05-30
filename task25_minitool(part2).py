#Adding a new feature i learnt called tk.Frame to the calorie counter and .pack_forget()
import tkinter as tk

daily_limit = 0

food_names = []
calorie_values = []


def set_goal():
    global daily_limit
    goal = goal_entry.get()
    if goal.isdigit():
        daily_limit = int(goal)
        goal_label.config(text = "")
        goal_prompt.pack_forget()
        goal_entry.pack_forget()
        goal_button.pack_forget()
        change_button.pack(pady=5)
        food_frame.pack(pady=10)
        update_total()
    else:
        goal_label.config(text = "Please enter a valid number", fg="red")

def change_goal():
    food_frame.pack_forget()
    change_button.pack_forget()
    goal_prompt.pack()
    goal_entry.pack(pady=5)
    goal_button.pack()
    goal_entry.delete(0,tk.END)
    goal_label.config(text = "Enter a new calorie goal", fg="#000080", font = ("Arial",10,"bold"))

def update_total():
    total = 0
    for values in calorie_values:
        total += values
    total_calories.config(text = f"Daily Goal: {daily_limit} calories | Current Total: {total} calories")

    if total < daily_limit:
        remaining = daily_limit - total
        limit.config(text = f"You can still eat {remaining} calories today", fg = "#AE33FA", font=("Arial",10))

    elif total == daily_limit:
        limit.config(text = "You have reached your calorie goal exactly!", fg = "#F906B0", font=("Arial",10))

    else:
        over = total - daily_limit
        limit.config(text = f"You are {over} calories over your limit", fg = "red", font=("Arial",10))


def add():
    food = food_entry.get()
    calories = calories_entry.get()
    if food.strip() == "":
        status_label.config(text = "Error: Food name cannot be blank", fg = "red")
    elif food.isdigit() == True:
        status_label.config(text = "Error: Food cannot be a number", fg = "red")

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

goal_prompt = tk.Label(window, text = "Enter Daily Calorie Goal: ", font= ("Times New Roman", 14 , "bold"))
goal_prompt.pack()
goal_entry = tk.Entry(window, width=25)
goal_entry.pack(pady=5)
goal_button = tk.Button(window, text = "Set Goal", command=set_goal)
goal_button.pack()
goal_label = tk.Label(window, text = "")
goal_label.pack()

food_frame = tk.Frame(window)
    
tk.Label(food_frame, text = "Enter a Food: ", font= ("Times New Roman", 12 , "bold")).pack(pady=5)
food_entry = tk.Entry(food_frame, width=25)
food_entry.pack()

tk.Label(food_frame, text = f"Enter Calories : ", font= ("Times New Roman", 12 , "bold")).pack(pady=5)
calories_entry = tk.Entry(food_frame, width=25)
calories_entry.pack()

tk.Button(food_frame, text = "Add Food", command = add).pack(pady=5)
length = tk.Label(food_frame, text = "")
length.pack()

status_label = tk.Label(food_frame, text="Waiting for input...", font=("Times New Roman", 10, "italic"), fg="gray")
status_label.pack()


food_list = tk.Listbox(food_frame, width = 35, height = 7)
food_list.pack()
food_list.bind("<<ListboxSelect>>", show)

total_calories = tk.Label(window, text = "Daily Goal: 0 calories | Current Total: 0 calories", font = ("Arial",10, "bold"), fg="purple")
total_calories.pack()

limit = tk.Label(food_frame, text = "")
limit.pack()

select = tk.Label(food_frame, text = "")
select.pack()

tk.Button(food_frame, text = "Delete Selected", command= delete).pack(pady=3)
tk.Button(food_frame, text = "Clear All", command= clear).pack(pady=3)

change_button = tk.Button(window, text = "Change Goal", command = change_goal)


window.mainloop()