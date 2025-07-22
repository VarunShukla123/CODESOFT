# PASSWORD GENERATOR
import tkinter as tk
from tkinter import messagebox
import random
import string
def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            messagebox.showerror("Error", "Enter a positive number")
            return
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        result_label.config(text="Password: " + password)
    except ValueError:
        messagebox.showerror("Error", "Enter a valid number")
root = tk.Tk()
root.title("Password Generator")
root.geometry("300x200")
tk.Label(root, text="Enter password length:").pack(pady=10)
length_entry = tk.Entry(root)
length_entry.pack()

tk.Button(root, text="Generate", command=generate_password).pack(pady=10)

result_label = tk.Label(root, text="Password: ")
result_label.pack()

tk.Button(root, text="Exit", command=root.destroy).pack(pady=10)

# Run the GUI loop
root.mainloop()
