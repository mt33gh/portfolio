"""
TITLE: Rock Paper Scissors with GUI by tkinter
DESCRIPTION: Given a Rock Paper Scissors code, I added GUI to it using tkinter.
    You need to create a sounds and pictures folder that includes win.mp3,
    lose.mp3, tie.mp3, rock.png, paper.png, scissors.png, and question.png 
LANGUAGE: Python 3
DATE: March 23, 2025
UPDATED: 
WRITTEN BY: Mitsuhiro Tagata
"""


import random
import tkinter as tk
from PIL import Image, ImageTk     #Use pillow
import sys
import os

# Suppress the pygame message
sys.stdout = open(os.devnull, 'w')
import pygame  # For sound effects
sys.stdout = sys.__stdout__  # Restore normal output

# Initialize pygame for sounds
pygame.mixer.init()

# Load sound effects
win_sound = pygame.mixer.Sound("sounds_and_pictures/win.mp3")
lose_sound = pygame.mixer.Sound("sounds_and_pictures/lose.mp3")
tie_sound = pygame.mixer.Sound("sounds_and_pictures/tie.mp3")

# Function to play the game
def play(player_choice):
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)

    # Update images
    player_img_label.config(image=images[player_choice])
    computer_img_label.config(image=images[computer_choice])

    # Determine the result
    if player_choice == computer_choice:
        result = "It's a tie!"
        tie_sound.play()
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "paper" and computer_choice == "rock") or \
         (player_choice == "scissors" and computer_choice == "paper"):
        result = "You win!"
        win_sound.play()
    else:
        result = "Computer wins!"
        lose_sound.play()
    
    result_label.config(text=result)

# Create the main window
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("670x700+100+50")  # width=670, height=700, x_offset=100, y_offset=50
root.configure(bg="#99ffe6")  # Light lavender background

# Label for instructions
instructions = tk.Label(root, text="Choose Rock, Paper, or Scissors:", font=("Arial", 18), bg="#99ffe6")
instructions.grid(row=0, column=0, padx=(90, 0), pady=10)

# Open the original images
original_rock = Image.open("sounds_and_pictures/rock.png")
original_paper = Image.open("sounds_and_pictures/paper.png")
original_scissors = Image.open("sounds_and_pictures/scissors.png")
original_question = Image.open("sounds_and_pictures/question.png")

# Resize while keeping aspect ratio
max_size = (200, 200)  # Set the maximum size
original_rock.thumbnail(max_size)  # This resizes while keeping the aspect ratio
original_paper.thumbnail(max_size)
original_scissors.thumbnail(max_size)
original_question.thumbnail(max_size)

# Convert to Tkinter-compatible format
images = {
    "rock": ImageTk.PhotoImage(original_rock),
    "paper": ImageTk.PhotoImage(original_paper),
    "scissors": ImageTk.PhotoImage(original_scissors),
    "question": ImageTk.PhotoImage(original_question)  # Default image for computer choice
}

# Labels for images
player_img_label = tk.Label(root, text="player", font=("Arial", 18), image=images["question"], compound="right", bg="#99ffe6")
player_img_label.grid(padx=120,pady=10, row=1, column=0, sticky="e")
computer_img_label = tk.Label(root, text="computer", font=("Arial", 18), image=images["question"], compound="right", bg="#99ffe6")
computer_img_label.grid(padx=120, pady=10, row=2, column=0, sticky="e")

# Buttons for choices
button_frame = tk.Frame(root, bg="#99ffe6")
button_frame.grid(row=3, column=0, padx=(90, 0), pady=10)
#button_frame.place(x=80, y=520)

tk.Button(button_frame, text="Rock", font=("Arial", 18), width=10, command=lambda: play("rock")).grid(row=0, column=0, padx=5)
tk.Button(button_frame, text="Paper", font=("Arial", 18), width=10, command=lambda: play("paper")).grid(row=0, column=1, padx=5)
tk.Button(button_frame, text="Scissors", font=("Arial", 18), width=10, command=lambda: play("scissors")).grid(row=0, column=2, padx=5)

# Label to display result
result_label = tk.Label(root, text="Before choosing", font=("Arial", 20, "bold"), bg="#99ffe6", fg="darkblue")
result_label.grid(row=4, column=0, padx=(90, 0), pady=20)
#result_label.place(x=250, y=600)

# Run the GUI
root.mainloop()
