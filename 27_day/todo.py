import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task:
        task_list.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task():
    try:
        selected_task = task_list.curselection()
        task_list.delete(selected_task)
    except:
        messagebox.showwarning("Warning", "Please select a task to delete.")

# Main window
root = tk.Tk()
root.title("To-Do List")

task_entry = tk.Entry(root, width=25)
task_entry.pack()

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack()

task_list = tk.Listbox(root, width=40, height=10)
task_list.pack()

delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.pack()

root.mainloop()
