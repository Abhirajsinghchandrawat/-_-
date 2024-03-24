import tkinter as tk
from tkinter import ttk
import random
import string

def generate_password():
    length = int(length_entry.get())
    password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length))
    password_var.set(password)

def copy_to_clipboard():
    password = password_var.get()
    root.clipboard_clear()
    root.clipboard_append(password)

    copied_label.config(text="Copied to clipboard!", fg="green")

root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")
root.resizable(False, False)
root.configure(bg="#f0f0f0")

title_label = tk.Label(root, text="Strong Password Generator", font=("Arial", 16, "bold"), bg="#f0f0f0")
title_label.pack(pady=10)

length_label = tk.Label(root, text="Password Length:", font=("Arial", 12), bg="#f0f0f0")
length_label.pack(pady=5)

length_entry = tk.Entry(root, font=("Arial", 12), width=10)
length_entry.pack(pady=5)
length_entry.insert(0, "12")

generate_button = ttk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack(pady=5)

password_var = tk.StringVar()
password_entry = tk.Entry(root, textvariable=password_var, font=("Arial", 12), width=30, bd=0, state="readonly", readonlybackground="#f0f0f0")
password_entry.pack(pady=10)

copy_button = ttk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.pack(pady=5)

copied_label = tk.Label(root, text="", font=("Arial", 10), bg="#f0f0f0")
copied_label.pack(pady=5)

root.mainloop()
