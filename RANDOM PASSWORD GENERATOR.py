import tkinter as tk
from tkinter import messagebox
import random
import string

# --- Password Generation Function ---
def generate_password():
    length = length_var.get()
    use_upper = upper_var.get()
    use_lower = lower_var.get()
    use_digits = digit_var.get()
    use_symbols = symbol_var.get()

    if not any([use_upper, use_lower, use_digits, use_symbols]):
        messagebox.showwarning("Weak Settings", "Select at least one character type!")
        return

    if length < 6:
        messagebox.showwarning("Too Short", "Password length should be at least 6 characters.")
        return

    chars = ""
    if use_upper:
        chars += string.ascii_uppercase
    if use_lower:
        chars += string.ascii_lowercase
    if use_digits:
        chars += string.digits
    if use_symbols:
        chars += string.punctuation

    password = ''.join(random.choice(chars) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)
    
    # Automatically copy to clipboard
    root.clipboard_clear()
    root.clipboard_append(password)
    messagebox.showinfo("Password Copied", "Password copied to clipboard!")

# Manual copy to clipboard
def copy_password():
    password = password_entry.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    else:
        messagebox.showwarning("No Password", "Generate a password first.")

# --- GUI Setup ---
root = tk.Tk()
root.title("Advanced Password Generator")
root.geometry("400x400")
root.resizable(False, False)

# --- Fonts ---
LABEL_FONT = ("Helvetica", 12)
BUTTON_FONT = ("Helvetica", 11, "bold")

# --- Widgets ---
tk.Label(root, text="Password Generator", font=("Helvetica", 16, "bold")).pack(pady=10)

# Password length
tk.Label(root, text="Password Length:", font=LABEL_FONT).pack()
length_var = tk.IntVar(value=12)
tk.Spinbox(root, from_=6, to=32, textvariable=length_var, font=LABEL_FONT, width=5).pack(pady=5)

# Complexity checkboxes
upper_var = tk.BooleanVar(value=True)
lower_var = tk.BooleanVar(value=True)
digit_var = tk.BooleanVar(value=True)
symbol_var = tk.BooleanVar(value=False)

tk.Checkbutton(root, text="Include Uppercase (A-Z)", variable=upper_var, font=LABEL_FONT).pack(anchor="w", padx=20)
tk.Checkbutton(root, text="Include Lowercase (a-z)", variable=lower_var, font=LABEL_FONT).pack(anchor="w", padx=20)
tk.Checkbutton(root, text="Include Digits (0-9)", variable=digit_var, font=LABEL_FONT).pack(anchor="w", padx=20)
tk.Checkbutton(root, text="Include Symbols (!@#)", variable=symbol_var, font=LABEL_FONT).pack(anchor="w", padx=20)

# Generate button
tk.Button(root, text="Generate Password", font=BUTTON_FONT, bg="#4CAF50", fg="white", command=generate_password).pack(pady=15)

# Entry to display password
password_entry = tk.Entry(root, font=("Courier", 14), justify="center", width=30)
password_entry.pack(pady=5)

# Copy button
tk.Button(root, text="Copy to Clipboard", font=BUTTON_FONT, bg="#2196F3", fg="white", command=copy_password).pack(pady=5)

# --- Start GUI Loop ---
root.mainloop()