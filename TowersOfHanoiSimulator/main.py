import tkinter as tk
from tkinter import messagebox


class TowersOfHanoi:
    def __init__(self, root, num_disks=3):
        self.root = root
        self.num_disks = num_disks
        self.rods = [list(range(num_disks, 0, -1)), [], []]
        self.canvas = tk.Canvas(root, width=600, height=400)
        self.canvas.pack()
        self.draw_rods()
        self.create_buttons()

    def draw_rods(self):
        # Clear the canvas
        self.canvas.delete("all")

        rod_width = 10
        rod_height = 300
        rod_x = [100, 300, 500]

        # Draw the rods
        for x in rod_x:
            self.canvas.create_rectangle(
                x - rod_width / 2, 50, x + rod_width / 2, 50 + rod_height, fill="brown")

        # Draw the disks on the rods
        for i, rod in enumerate(self.rods):
            y = 350
            for disk in rod:
                disk_width = disk * 20
                self.canvas.create_rectangle(
                    rod_x[i] - disk_width / 2, y, rod_x[i] + disk_width / 2, y - 10, fill="blue")
                y -= 10

    def create_buttons(self):
        # Create the Reset button
        tk.Button(self.root, text="Reset",
                  command=self.reset).place(x=250, y=10)

        # Create the Play button
        tk.Button(self.root, text="Play", command=self.play).place(x=310, y=10)

    def reset(self):
        # Reset the rods to their initial state
        self.rods = [list(range(self.num_disks, 0, -1)), [], []]
        self.draw_rods()

    def play(self):
        # Start the solving process
        self.solve()

    def solve(self):
        # Solve the Towers of Hanoi problem
        self.solve_hanoi(self.num_disks, 0, 2, 1)

    def solve_hanoi(self, n, from_rod, to_rod, aux_rod):
        if n == 1:
            # Move the top disk from the source rod to the destination rod
            self.rods[to_rod].append(self.rods[from_rod].pop())
            self.draw_rods()
            self.root.update()
            self.root.after(500)
        else:
            # Move n-1 disks from the source rod to the auxiliary rod
            self.solve_hanoi(n - 1, from_rod, aux_rod, to_rod)

            # Move the remaining disk from the source rod to the destination rod
            self.rods[to_rod].append(self.rods[from_rod].pop())
            self.draw_rods()
            self.root.update()
            self.root.after(500)

            # Move the n-1 disks from the auxiliary rod to the destination rod
            self.solve_hanoi(n - 1, aux_rod, to_rod, from_rod)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Towers of Hanoi")
    app = TowersOfHanoi(root)
    root.mainloop()
