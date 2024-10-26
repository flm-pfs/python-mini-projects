import tkinter as tk
from tkinter import messagebox
import random

class BingoGame:
	def __init__(self, root, player_name):
		self.root = root
		self.player_name = player_name
		self.root.title(f"{player_name}'s Bingo Game")

		self.card = self.generate_card()
		self.create_widgets()
		self.cross_count = 0

	@staticmethod
	def generate_card():
		card = []
		numbers = random.sample(range(1, 76), 25)
		for i in range(0, 25, 5):
			row = numbers[i:i+5]
			card.append(row)
		return card

	def create_widgets(self):
		self.buttons = []
		for i in range(5):
			row = []
			for j in range(5):
				btn = tk.Button(self.root, text=str(self.card[i][j]), width=10, height=3,
								command=lambda i=i, j=j: self.cross_number(i, j))
				btn.grid(row=i, column=j)
				row.append(btn)
			self.buttons.append(row)

	def cross_number(self, i, j):
		if self.buttons[i][j]['bg'] != 'green':
			self.buttons[i][j].config(bg='green')
			self.check_bingo()

	def check_bingo(self):
		# Check rows
		for row in self.buttons:
			if all(btn['bg'] == 'green' for btn in row):
				self.cross_count += 1
				for btn in row:
					btn.config(state=tk.DISABLED)

		# Check columns
		for j in range(5):
			if all(self.buttons[i][j]['bg'] == 'green' for i in range(5)):
				self.cross_count += 1
				for i in range(5):
					self.buttons[i][j].config(state=tk.DISABLED)

		# Check diagonals
		if all(self.buttons[i][i]['bg'] == 'green' for i in range(5)):
			self.cross_count += 1
			for i in range(5):
				self.buttons[i][i].config(state=tk.DISABLED)
		if all(self.buttons[i][4-i]['bg'] == 'green' for i in range(5)):
			self.cross_count += 1
			for i in range(5):
				self.buttons[i][4-i].config(state=tk.DISABLED)

		if self.cross_count >= 5:
			self.show_bingo()

	def show_bingo(self):
		messagebox.showinfo("Bingo!", f"Congratulations {self.player_name}! You have a Bingo!")
		self.root.quit()


if __name__ == "__main__":
	root = tk.Tk()
	game1 = BingoGame(root, "Player 1")
	root.mainloop()
