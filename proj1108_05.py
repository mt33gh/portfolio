"""
TITLE: Simple calculator with GUI by tkinter and ttk
DESCRIPTION: Given a simple calculater code, I added GUI to it using tkinter and ttk.
LANGUAGE: Python 3
DATE: June 3, 2025
UPDATED: 
WRITTEN BY: Mitsuhiro Tagata
"""


import tkinter as tk
from tkinter import ttk

#Retrieve and validate user input from entry fields
def get_numbers():
    num1_text = entry2.get().strip()
    num2_text = entry3.get().strip()
    num1 = float(num1_text)
    num2 = float(num2_text)
    return num1, num2    #Return a tuple

# Calculator functions
def add():
    numbers = get_numbers()
    num1, num2 = numbers
    result.set(num1 + num2)
def subtract():
    numbers = get_numbers()
    num1, num2 = numbers
    result.set(num1 - num2)
def multiply():
    numbers = get_numbers()
    num1, num2 = numbers
    result.set(num1 * num2)
def divide():
    numbers = get_numbers()
    num1, num2 = numbers
    result.set(num1 / num2)

# Create the main window
root = tk.Tk()
root.geometry("600x400")
root.configure(bg="lightblue")
root.title("My Calculator: June 2025")

style = ttk.Style()
#style.theme_use("clam")
style.configure("My.TButton", font=("Arial", 28))
style.configure("My.TFrame", background="blue")
style.configure("My.TLabel", font=("Arial", 28), background="yellow")
style.configure("My.TEntry", foreground="red", font=("Arial", 28))  # somehow, font doesn't work here
#print(style.theme_use())

root.columnconfigure(0, weight=1)
# frame1
frame1 = ttk.Frame(root, padding=20, style="My.TFrame")
frame1.grid(row=0, column=0)
frame1.columnconfigure((1, 2, 3, 4), weight=1)  # two columns in frame
lbl = ttk.Label(frame1,text="Press a Button", style="My.TLabel")
lbl.grid(row=0,column=0,padx=10)
btnA = ttk.Button(frame1,text="+", command=add, style="My.TButton") 
btnA.grid(row=0,column=1,padx=10)
btnB = ttk.Button(frame1,text="-", command=subtract, style="My.TButton") 
btnB.grid(row=0,column=2,padx=10)
btnC = ttk.Button(frame1,text="*", command=multiply, style="My.TButton") 
btnC.grid(row=0,column=3,padx=10)
btnD = ttk.Button(frame1,text="/", command=divide, style="My.TButton") 
btnD.grid(row=0,column=4,padx=10)

# frame2
frame2 = ttk.Frame(root, padding=20, style="My.TFrame")
frame2.grid(row=1, column=0)
frame2.columnconfigure((0, 1), weight=1)  # two columns in frame
lbl2 = ttk.Label(frame2,text="Label 1", style="My.TLabel")
lbl2.grid(row=0,column=0,padx=10)
entry2 = ttk.Entry(frame2, font=("Arial", 20), style="My.TEntry")
entry2.grid(row=0, column=1, padx=10)

# frame3
frame3 = ttk.Frame(root, padding=20, style="My.TFrame")
frame3.grid(row=2, column=0)
frame3.columnconfigure((0, 1), weight=1)  # two columns in frame
lbl3 = ttk.Label(frame3,text="Label 1", style="My.TLabel")
lbl3.grid(row=0,column=0,padx=10)
entry3 = ttk.Entry(frame3, font=("Arial", 20), style="My.TEntry")
entry3.grid(row=0, column=1, padx=10)

# Result display
result = tk.StringVar(value="not calculated yet")
frame4 = ttk.Frame(root, padding=20, style="My.TFrame")
frame4.grid(row=3, column=0)
frame4.columnconfigure((0, 1), weight=1)  # two columns in frame
lbl4 = ttk.Label(frame4, text="Result: ", style="My.TLabel")
lbl4.grid(row=0,column=0,padx=10)
lbl5 = ttk.Label(frame4, textvariable=result, font=("Arial", 20, "bold"), style="My.TLabel")
lbl5.grid(row=0, column=1, padx=10)

root.mainloop()

