#TO-D0-LIST
import tkinter as tk
from tkinter import messagebox
root = tk.Tk()
root.title("To-Do List")
root.geometry("200*400")

tasks = []
def add_task():
    task = task_entry.get()
    if task != "":
        tasks.append(task)
        listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task!")
def delete_task():
    selected = listbox.curselection()
    if selected:
        task_index = selected[0]
        listbox.delete(task_index)
        tasks.pop(task_index)
    else:
        messagebox.showwarning("Warning", "Please select a task to delete.")
task_entry = tk.Entry(root, width=30)
task_entry.pack(pady=10)
add_btn = tk.Button(root, text="Add Task", command=add_task)
add_btn.pack(pady=5)

listbox = tk.Listbox(root, width=30, height=10)
listbox.pack(pady=10)
delete_btn = tk.Button(root, text="Delete Task", command=delete_task)
delete_btn.pack(pady=5)
root.mainloop()
