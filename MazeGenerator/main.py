import tkinter as tk
import random
import sys

sys.setrecursionlimit(10**6)  # Set the recursion limit to a higher value


class MazeGenerator:
    def __init__(self, master, width=50, height=50, cell_size=10):
        self.master = master
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.canvas = tk.Canvas(master, width=width *
                                cell_size, height=height*cell_size)
        self.canvas.pack()
        self.maze = [[{'top': True, 'right': True, 'bottom': True, 'left': True,
                       'visited': False} for _ in range(height)] for _ in range(width)]
        self.generate_maze(0, 0)
        self.draw_maze()

    def generate_maze(self, x, y):
        # Mark the current cell as visited
        self.maze[x][y]['visited'] = True
        directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
        random.shuffle(directions)
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            # Check if the neighboring cell is within the maze boundaries and not visited
            if 0 <= nx < self.width and 0 <= ny < self.height and not self.maze[nx][ny]['visited']:
                # Remove the wall between the current cell and the neighboring cell
                if dx == -1:
                    self.maze[x][y]['left'] = False
                    self.maze[nx][ny]['right'] = False
                elif dx == 1:
                    self.maze[x][y]['right'] = False
                    self.maze[nx][ny]['left'] = False
                elif dy == -1:
                    self.maze[x][y]['top'] = False
                    self.maze[nx][ny]['bottom'] = False
                elif dy == 1:
                    self.maze[x][y]['bottom'] = False
                    self.maze[nx][ny]['top'] = False
                # Recursively generate the maze starting from the neighboring cell
                self.generate_maze(nx, ny)

    def draw_maze(self):
        for x in range(self.width):
            for y in range(self.height):
                cell = self.maze[x][y]
                x1, y1 = x * self.cell_size, y * self.cell_size
                x2, y2 = x1 + self.cell_size, y1 + self.cell_size
                # Draw the walls of the cell based on the maze configuration
                if cell['top']:
                    self.canvas.create_line(x1, y1, x2, y1)
                if cell['right']:
                    self.canvas.create_line(x2, y1, x2, y2)
                if cell['bottom']:
                    self.canvas.create_line(x2, y2, x1, y2)
                if cell['left']:
                    self.canvas.create_line(x1, y2, x1, y1)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Maze Generator")
    maze = MazeGenerator(root)
    root.mainloop()
