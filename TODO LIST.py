#TO-D0-LIST
import tkinter as tk
from tkinter import messagebox
root = tk.Tk()
root.title("Simple To-Do List")
root.geometry("300x420")
tasks = []
def add_task():
    task = task_entry.get()
    if task:
        tasks.append(task)
        listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task!")
def delete_task():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        listbox.delete(index)
        tasks.pop(index)
    else:
        messagebox.showwarning("Warning", "Please select a task to delete.")
def exit_app():
    root.destroy()
task_entry = tk.Entry(root, width=30)
task_entry.pack(pady=10)
tk.Button(root, text="Add Task", command=add_task).pack(pady=5)
tk.Button(root, text="Delete Task", command=delete_task).pack(pady=5)
listbox = tk.Listbox(root, width=30, height=10)
listbox.pack(pady=10)
tk.Button(root, text="Exit", command=exit_app, fg="white", bg="red").pack(pady=10)
root.mainloop()
