import random
import string
import tkinter as tk
from tkinter import messagebox

# -----------------------------
# Strong Password Generator
# -----------------------------

def generate_password():
    username = name_entry.get().strip()

    if username == "":
        messagebox.showwarning("Input Required", "Please enter your username.")
        return

    # Remove spaces from username
    username = username.replace(" ", "")

    # Characters for password
    letters = string.ascii_letters
    numbers = string.digits
    symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?/"

    # Use part of username (maximum 4 characters)
    name_part = username[:4]

    # Random characters
    random_letters = ''.join(random.choice(letters) for _ in range(4))
    random_numbers = ''.join(random.choice(numbers) for _ in range(3))
    random_symbols = ''.join(random.choice(symbols) for _ in range(3))

    # Combine everything
    password_list = list(name_part + random_letters + random_numbers + random_symbols)
    random.shuffle(password_list)

    password = ''.join(password_list)

    # Display password
    password_entry.config(state="normal")
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)
    password_entry.config(state="readonly")


def copy_password():
    password = password_entry.get()

    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        root.update()
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    else:
        messagebox.showwarning("No Password", "Generate a password first.")


# -----------------------------
# GUI
# -----------------------------

root = tk.Tk()
root.title("Strong Password Generator")
root.geometry("1000x700")
root.resizable(False, False)

title = tk.Label(
    root,
    text="Strong Password Generator",
    font=("Arial", 16, "bold")
)
title.pack(pady=15)

tk.Label(root, text="Username", font=("Arial", 11)).pack()

name_entry = tk.Entry(root, font=("Arial", 12), width=30)
name_entry.pack(pady=5)

generate_btn = tk.Button(
    root,
    text="Generate Password",
    font=("Arial", 11, "bold"),
    width=20,
    command=generate_password
)
generate_btn.pack(pady=10)

tk.Label(root, text="Generated Password", font=("Arial", 11)).pack()

password_entry = tk.Entry(
    root,
    font=("Consolas", 12),
    width=30,
    justify="center",
    state="readonly"
)
password_entry.pack(pady=5)

copy_btn = tk.Button(
    root,
    text="Copy Password",
    font=("Arial", 11),
    width=20,
    command=copy_password
)
copy_btn.pack(pady=10)

root.mainloop()
