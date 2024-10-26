import tkinter as tk
from tkinter import messagebox
import random


class MemoryGame:
    def __init__(self, master, rows=4, cols=4):
        self.master = master
        self.rows = rows
        self.cols = cols
        self.cards = []  # List to store the card objects
        self.flipped = []  # List to store the flipped cards
        self.matched = []  # List to store the matched cards
        self.create_cards()  # Create the cards
        self.create_board()  # Create the game board
        self.first_flip = None

    def create_cards(self):
        values = list(range(1, (self.rows * self.cols) // 2 + 1)) * 2
        random.shuffle(values)
        self.cards = [Card(self, value)
                      for value in values]  # Create card objects

    def create_board(self):
        for i, card in enumerate(self.cards):
            row = i // self.cols
            col = i % self.cols
            # Position the cards on the game board
            card.grid(row=row, column=col)

    def flip(self, card):
        if card in self.flipped or card in self.matched:
            return
        card.flip()  # Flip the card
        self.flipped.append(card)  # Add the flipped card to the list
        if len(self.flipped) == 2:
            self.check_match()  # Check if the flipped cards match

    def check_match(self):
        card1, card2 = self.flipped
        if card1.value == card2.value:
            # Add the matched cards to the list
            self.matched.extend([card1, card2])
            if len(self.matched) == len(self.cards):
                # Show a message box when all cards are matched
                messagebox.showinfo("Congratulations!", "You've won the game!")
        else:
            # Reset the flipped cards after 1 second
            self.master.after(1000, self.reset_flipped)
        self.flipped = []  # Reset the flipped cards list

    def reset_flipped(self):
        for card in self.flipped:
            card.flip()  # Flip the cards back
        self.flipped = []  # Reset the flipped cards list


class Card(tk.Button):
    def __init__(self, game, value):
        self.game = game
        self.value = value
        self.flipped = False
        super().__init__(game.master, text="", width=10, height=4, command=self.on_flip)

    def on_flip(self):
        self.game.flip(self)  # Call the flip method of the game object

    def flip(self):
        self.flipped = not self.flipped
        # Set the text of the button based on the flipped state
        self.config(text=str(self.value) if self.flipped else "")


def main():
    root = tk.Tk()
    root.title("Memory Game")
    game = MemoryGame(root)  # Create the MemoryGame object
    root.mainloop()


if __name__ == "__main__":
    main()
