#CALCULATOR
import tkinter as tk

def calc():
    try:
        a, b = float(e1.get()), float(e2.get())
        op = op_entry.get()
        r = {'+': a + b, '-': a - b, '*': a * b, '/': a / b if b != 0 else 'Err'}[op]
        result.set(r)
    except:
        result.set("Error")

root = tk.Tk()
root.title("Calc"); root.geometry("250x250")

tk.Label(root, text="1st Number").pack()
e1 = tk.Entry(root); e1.pack()

tk.Label(root, text="2nd Number").pack()
e2 = tk.Entry(root); e2.pack()

tk.Label(root, text="Operator (+ - * /)").pack()
op_entry = tk.Entry(root); op_entry.pack()

result = tk.StringVar()
tk.Label(root, textvariable=result, font=("Arial", 14)).pack(pady=10)

tk.Button(root, text="Calculate", command=calc).pack()
tk.Button(root, text="Exit", command=root.destroy).pack(pady=5)

root.mainloop()
