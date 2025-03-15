"""
TITLE: Simple calculator with GUI by tkinter
DESCRIPTION: Given a simple calculater code, I added GUI to it using tkinter.
LANGUAGE: Python 3
DATE: March 15, 2025
UPDATED: 
WRITTEN BY: Mitsuhiro Tagata
"""


import tkinter as tk
from tkinter import messagebox

#Retrieve and validate user input from entry fields
def get_numbers():
    num1_text = entry1.get().strip()
    num2_text = entry2.get().strip()
    if not num1_text or not num2_text:  # Check if either input is empty
        messagebox.showerror("Input Error", "Both numbers must be entered.")
        return None
    try:
        num1 = float(num1_text)
        num2 = float(num2_text)
        return num1, num2         #Return a tuple
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")
        return None # Return None if input is invalid

# Calculator functions
def add():
    numbers = get_numbers()
    if numbers: # If numbers is not None
        num1, num2 = numbers
        result.set(num1 + num2)
def subtract():
    numbers = get_numbers()
    if numbers:
        num1, num2 = numbers
        result.set(num1 - num2)
def multiply():
    numbers = get_numbers()
    if numbers:
        num1, num2 = numbers
        result.set(num1 * num2)
def divide():
    numbers = get_numbers()
    if numbers:
        num1, num2 = numbers
        if num2 == 0:
            messagebox.showerror("Math Error", "Cannot divide by zero.")
        else:
            result.set(num1 / num2)

# Create main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("500x400")
root.configure(bg="lightgreen")  # Changes the window background color

# Set a larger default font
root.option_add("*Font", ("Arial", 16))

# Create a large title
title_label = tk.Label(root, text="Simple Calculator", font=("Arial", 24, "bold"), bg="yellow", fg="blue")
title_label.grid(row=0, column=0, columnspan=2, pady=10)

# Input fields
tk.Label(root, text="Enter first number:", bg="orange", fg="purple").grid(row=1, column=0, padx=10, sticky="w")
entry1 = tk.Entry(root)
entry1.grid(row=1, column=1, padx=10)

tk.Label(root, text="Enter second number:", bg="pink", fg="green").grid(row=2, column=0, padx=10, sticky="w")
entry2 = tk.Entry(root)
entry2.grid(row=2, column=1, padx=10)

# Blank space row=3
root.grid_rowconfigure(3, minsize=30) # Adjust 30 to control the blank space

# Buttons for operations
tk.Button(root, text="+", command=add, bg="lightblue", fg="blue", relief="raised", bd=3).grid(row=4, column=0)
tk.Button(root, text="-", command=subtract, bg="lightblue", fg="blue", relief="raised", bd=3).grid(row=4, column=1)
tk.Button(root, text="*", command=multiply, bg="lightblue", fg="blue", relief="raised", bd=3).grid(row=5, column=0)
tk.Button(root, text="/", command=divide, bg="lightblue", fg="blue", relief="raised", bd=3).grid(row=5, column=1)

# Blank space row=6
root.grid_rowconfigure(6, minsize=30) # Adjust 30 to control the blank space

# Result display
result = tk.StringVar()
tk.Label(root, text="Result:  ").grid(row=7, column=0, sticky="e")
tk.Label(root, textvariable=result, font=("Arial", 16, "bold")).grid(row=7, column=1, sticky="w")

# Run the GUI loop
root.mainloop()