import tkinter as tk
from tkinter import messagebox
import random


class Minesweeper:
    def __init__(self, master, rows=10, cols=10, mines=10):
        self.master = master
        self.rows = rows
        self.cols = cols
        self.mines = mines
        self.buttons = [[None for _ in range(cols)] for _ in range(rows)]
        self.revealed = [[False for _ in range(cols)] for _ in range(rows)]
        self.mine_positions = set()
        self.create_board()
        self.place_mines()

    def create_board(self):
        for i in range(self.rows):
            for j in range(self.cols):
                button = tk.Button(self.master, text='', width=2, height=1,
                                   command=lambda row=i, col=j: self.reveal(row, col))
                button.grid(row=i, column=j)
                self.buttons[i][j] = button

    def place_mines(self):
        while len(self.mine_positions) < self.mines:
            row = random.randint(0, self.rows - 1)
            col = random.randint(0, self.cols - 1)
            self.mine_positions.add((row, col))

    def reveal(self, row, col):
        if (row, col) in self.mine_positions:
            self.buttons[row][col].config(text='*', bg='red')
            self.game_over()
        else:
            mines_count = self.count_adjacent_mines(row, col)
            self.buttons[row][col].config(
                text=str(mines_count), state=tk.DISABLED, bg='gray')
            self.revealed[row][col] = True
            if mines_count == 0:
                self.reveal_adjacent(row, col)

    def count_adjacent_mines(self, row, col):
        count = 0
        for i in range(max(0, row-1), min(row+2, self.rows)):
            for j in range(max(0, col-1), min(col+2, self.cols)):
                if (i, j) in self.mine_positions:
                    count += 1
        return count

    def reveal_adjacent(self, row, col):
        for i in range(max(0, row-1), min(row+2, self.rows)):
            for j in range(max(0, col-1), min(col+2, self.cols)):
                if not self.revealed[i][j]:
                    self.reveal(i, j)

    def game_over(self):
        for (row, col) in self.mine_positions:
            self.buttons[row][col].config(text='*', bg='red')
        for i in range(self.rows):
            for j in range(self.cols):
                self.buttons[i][j].config(state=tk.DISABLED)
        messagebox.showinfo("Game Over", "You hit a mine!")
        root.quit()


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Minesweeper")
    game = Minesweeper(root)
    root.mainloop()
