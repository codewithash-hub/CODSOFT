import tkinter as tk
from tkinter import ttk
from customtkinter import *
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


root = CTk()
root.title("Password Generator")
root.geometry("300x300")

len_var = tk.StringVar(value=0)
res_var = tk.StringVar()

ttk.Label(root, text="Password Length:").pack(pady=5)
ttk.Entry(root, textvariable=len_var, width=5).pack()

btn = CTkButton(root, text="Generate", corner_radius=32, fg_color="#C850C0", hover_color="#4158D0", command=gen_password).pack(pady=10)

ttk.Label(root, text="Generate Password").pack()
ttk.Entry(root, textvariable=res_var, state="readonly").pack()

root.mainloop()