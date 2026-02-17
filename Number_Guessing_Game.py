import tkinter as tk
import random

# Create main window
root = tk.Tk()
root.title("Number Guessing Game")
root.geometry("500x400")
root.resizable(False, False)
root.configure(bg="#62d3dd")

# Game variables
secret_number = random.randint(1, 100)
max_attempt = 10
attempt = 0

# Function to check guess
def check_guess():
    global attempt, secret_number
    
    try:
        guess = int(entry.get())
    except ValueError:
        result_label.config(text="Please enter a valid number!")
        return

    attempt += 1
    attempts_left = max_attempt - attempt

    if guess == secret_number:
        result_label.config(text=f"🎉 Correct! You guessed in {attempt} attempts.",fg="white",bg="green")
        submit_btn.config(state="disabled")
    elif guess > secret_number:
        result_label.config(text="Too High!",fg="white",bg="red")
    else:
        result_label.config(text="Too Low!",fg="white",bg="red")

    attempts_label.config(text=f"Attempts Left: {attempts_left}")

    if attempt == max_attempt and guess != secret_number:
        result_label.config(text=f"Game Over! Number was {secret_number}")
        submit_btn.config(state="disabled")

    entry.delete(0, tk.END)

# Function to restart game
def restart_game():
    global attempt, secret_number
    secret_number = random.randint(1, 100)
    attempt = 0
    result_label.config(text="")
    attempts_label.config(text=f"Attempts Left: {max_attempt}")
    submit_btn.config(state="normal")
    entry.delete(0, tk.END)

# UI Elements
title_label = tk.Label(root, text="🧠 Guess the Number (1-100) 🎯", font=("Arial", 16),bg="#ffffff",fg="#000000",width=25)
title_label.pack(pady=10)

entry = tk.Entry(root, font=("Arial", 14),bg="#c773de", width=15, justify='center')
entry.pack(pady=5)

submit_btn = tk.Button(root, text="Submit Guess", font=("Arial", 12), command=check_guess,
                       bg="#2A2323",fg="white", width=12)
submit_btn.pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 12),bg="#62d3dd")
result_label.pack(pady=5)

attempts_label = tk.Label(root, text=f"Attempts Left: {max_attempt}", font=("Arial", 12),bg="#254cdb",fg="white")
attempts_label.pack(pady=5)

restart_btn = tk.Button(root, text="Restart Game", font=("Arial", 12), command=restart_game,bg="#D31818",fg="white", width=12)
restart_btn.pack(pady=10)

root.mainloop()
