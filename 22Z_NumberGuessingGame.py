#**************** Your Task *************
# This code is for studying tkinter.

import random
import tkinter as tk
from tkinter import messagebox

# Generate random number
number = random.randint(1, 100)

def check_guess():
    try:
        guess = int(entry.get())
        if guess < number:
            result_label.config(text="Too low!")
        elif guess > number:
            result_label.config(text="Too high!")
        else:
            #result_label.config(text="Congratulations!\nYou've got the right number.", justify="left")
            messagebox.showinfo("Congratulations!", "You've got the right number.")
            root.quit()
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")


# Create GUI window
root = tk.Tk()
root.title("Number Guessing Game")
root.geometry("400x200")
root.configure(bg="#ffff99")  # Changes the window background color to light yellow

# Set a larger default font
root.option_add("*Font", ("Arial", 16))

# Widgets
tk.Label(root, text="Guess a number between 1 and 100:", bg="#ffff99").pack(pady=10)
entry = tk.Entry(root)
entry.pack(pady=5)

guess_button = tk.Button(root, text="Submit Guess", command=check_guess, bg="#ccffff")
guess_button.pack(pady=5)

result_label = tk.Label(root, text="", bg="#ffff99") #"empty" is dummy
result_label.pack(pady=5)

# Run the main loop
root.mainloop()

