import tkinter as tk
from tkinter import ttk, messagebox
import random

class GuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")

        self.number_to_guess = random.randint(1, 100)
        self.attempts = 0

        self.create_widgets()

    def create_widgets(self):
        frame = ttk.Frame(self.root, padding="10")
        frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        self.label_instruction = ttk.Label(frame, text="I have selected a number between 1 and 100. Can you guess what it is?")
        self.label_instruction.grid(row=0, column=0, columnspan=2, sticky=tk.W)

        self.label_guess = ttk.Label(frame, text="Enter your guess:")
        self.label_guess.grid(row=1, column=0, sticky=tk.W)

        self.entry_guess = ttk.Entry(frame)
        self.entry_guess.grid(row=1, column=1, sticky=(tk.W, tk.E))

        self.button_guess = ttk.Button(frame, text="Submit Guess", command=self.check_guess)
        self.button_guess.grid(row=2, column=0, columnspan=2)

        self.result = tk.StringVar()
        self.label_result = ttk.Label(frame, textvariable=self.result, foreground="blue")
        self.label_result.grid(row=3, column=0, columnspan=2, sticky=(tk.W, tk.E))

        frame.columnconfigure(1, weight=1)

    def check_guess(self):
        try:
            guess = int(self.entry_guess.get())
            self.attempts += 1

            if guess < self.number_to_guess:
                self.result.set("Too low! Try again.")
            elif guess > self.number_to_guess:
                self.result.set("Too high! Try again.")
            else:
                self.result.set(f"Congratulations! You've guessed the number correctly in {self.attempts} attempts.")
                messagebox.showinfo("Congratulations!", f"You've guessed the number correctly in {self.attempts} attempts.")
                self.reset_game()
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter a valid integer.")

    def reset_game(self):
        self.number_to_guess = random.randint(1, 100)
        self.attempts = 0
        self.entry_guess.delete(0, tk.END)
        self.result.set("")

if __name__ == "__main__":
    root = tk.Tk()
    game = GuessingGame(root)
    root.mainloop()
