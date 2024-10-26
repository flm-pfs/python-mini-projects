import tkinter as tk
from tkinter import messagebox
import random


class DiceRoller:
    def __init__(self, master):
        self.master = master
        self.master.title("Dice Roller")
        self.master.geometry("300x200")

        self.result_label = tk.Label(
            self.master, text="Roll the dice!", font=("Helvetica", 24))
        self.result_label.pack(pady=20)

        self.roll_button = tk.Button(self.master, text="Roll", font=(
            "Helvetica", 16), command=self.roll_dice)
        self.roll_button.pack(pady=20)

    def roll_dice(self):
        result = random.randint(1, 6)
        self.result_label.config(text=str(result))


def main():
    root = tk.Tk()  # Create the main window
    app = DiceRoller(root)  # Create an instance of the DiceRoller class
    root.mainloop()  # Start the main event loop


if __name__ == "__main__":
    main()  # Call the main function to start the application
