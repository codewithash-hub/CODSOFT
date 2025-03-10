import tkinter as tk
from tkinter import ttk
from customtkinter import *
from CTkMessagebox import CTkMessagebox
import string
import random

def gen_password():
    try:
        length_of_password = int(len_var.get())

        char = string.ascii_letters
        char += string.digits
        char += string.punctuation

        password = ''.join(
            random.choice(char)
            for _ in range(length_of_password)
        )

        res_var.set(password)
    except ValueError:
        show_error()

def show_error():
    # Show some error message
    CTkMessagebox(title="Error", message="Error: You should enter a value.", icon="cancel")

root = CTk()
root.title("Password Generator")
root.geometry("300x300")
set_appearance_mode("dark")

len_var = tk.StringVar()
res_var = tk.StringVar()

CTkLabel(root, text="Password Length:").pack(pady=5)
CTkEntry(root, textvariable=len_var, width=150).pack()

btn = CTkButton(root, text="Generate", corner_radius=32, fg_color="#C850C0", hover_color="#4158D0", command=gen_password)
btn.place(relx=0.5, rely=0.5, anchor="center")

CTkLabel(root, text="Generate Password").pack()
CTkEntry(root, textvariable=res_var, state="readonly").pack()

root.mainloop()