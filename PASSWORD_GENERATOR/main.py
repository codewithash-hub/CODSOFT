import tkinter as tk
from tkinter import ttk
import string
import random

def gen_password():
    length_of_password = int(len_var.get())

    char = string.ascii_letters
    char += string.digits
    char += string.punctuation

    password = ''.join(
        random.choice(char)
        for _ in range(length_of_password)
    )

    res_var.set(password)


root = tk.Tk()
root.title("Password Generator")
root.geometry("300x150")

len_var = tk.StringVar(value=0)
res_var = tk.StringVar()

ttk.Label(root, text="Password Length:").pack(pady=5)
ttk.Entry(root, textvariable=len_var, width=5).pack()

ttk.Button(root, text="Generate", command=gen_password).pack(pady=10)

ttk.Label(root, text="Generate Password").pack()
ttk.Entry(root, textvariable=res_var, state="readonly").pack()

root.mainloop()