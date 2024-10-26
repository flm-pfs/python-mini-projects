import tkinter as tk
import random
from tkinter import messagebox

class CarGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Car Game")
        self.root.geometry("800x600")

        self.canvas = tk.Canvas(self.root, width=800, height=600, bg="white")
        self.canvas.pack()

        self.car = self.canvas.create_rectangle(
            380, 550, 420, 580, fill="blue")
        self.finish_line = self.canvas.create_line(
            0, 50, 800, 50, fill="green", width=5)

        self.root.bind("<Left>", self.move_left)
        self.root.bind("<Right>", self.move_right)
        self.root.bind("<Up>", self.move_up)
        self.root.bind("<Down>", self.move_down)

    def move_left(self, event):
        coords = self.canvas.coords(self.car)
        if coords[0] > 0:
            self.canvas.move(self.car, -10, 0)

    def move_right(self, event):
        coords = self.canvas.coords(self.car)
        if coords[2] < 800:
            self.canvas.move(self.car, 10, 0)

    def move_up(self, event):
        coords = self.canvas.coords(self.car)
        if coords[1] > 0:
            self.canvas.move(self.car, 0, -10)
            if self.check_collision():
                messagebox.showinfo("Congratulations", "You won!")
                self.root.destroy()

    def move_down(self, event):
        coords = self.canvas.coords(self.car)
        if coords[3] < 600:
            self.canvas.move(self.car, 0, 10)

    def check_collision(self):
        car_coords = self.canvas.coords(self.car)
        finish_line_coords = self.canvas.coords(self.finish_line)
        if (car_coords[1] <= finish_line_coords[1] and car_coords[3] >= finish_line_coords[1]):
            return True
        return False


if __name__ == "__main__":
    root = tk.Tk()
    game = CarGame(root)
    root.mainloop()
