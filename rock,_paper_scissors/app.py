"""rock paper game using tkinter module"""
import tkinter as tk
from tkinter import messagebox
import random

def play_game(player_choice):
    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)

    result = determine_winner(player_choice, computer_choice)

    message = f"Player chose {player_choice}\nComputer chose {computer_choice}\nResult: {result}"
    messagebox.showinfo("Result", message)

def determine_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    elif (
        (player == "Rock" and computer == "Scissors") or
        (player == "Paper" and computer == "Rock") or
        (player == "Scissors" and computer == "Paper")
    ):
        return "Player wins!"
    else:
        return "Computer wins!"

# GUI setup
root = tk.Tk()
root.title("Rock, Paper, Scissors Game")

rock_button = tk.Button(root, text="Rock", command=lambda: play_game("Rock"))
rock_button.pack(pady=10)

paper_button = tk.Button(root, text="Paper", command=lambda: play_game("Paper"))
paper_button.pack(pady=10)

scissors_button = tk.Button(root, text="Scissors", command=lambda: play_game("Scissors"))
scissors_button.pack(pady=10)

exit_button = tk.Button(root, text="Exit", command=root.destroy)
exit_button.pack(pady=10)

root.mainloop()
