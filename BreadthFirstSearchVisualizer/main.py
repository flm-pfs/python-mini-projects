import tkinter as tk
from tkinter import messagebox
from collections import deque


class BFSVisualizer:
    def __init__(self, size=10):
        self.size = size
        # Initialize the grid with all zeros
        self.grid = [[0 for _ in range(size)] for _ in range(size)]
        self.start = (2, 0)  # Set the start position
        self.end = (size - 1, size - 1)  # Set the end position
        self.visited = set()  # Set to keep track of visited nodes
        self.app = tk.Tk()  # Create the Tkinter application
        # Set the title of the application window
        self.app.title("BFS Visualizer")
        # Create a canvas for drawing
        self.canvas = tk.Canvas(self.app, width=size * 40, height=size * 40)
        self.canvas.pack()  # Pack the canvas into the application window
        self.draw_grid()  # Draw the initial grid
        # Start the BFS algorithm after 1 second
        self.app.after(1000, self.bfs, self.start)
        self.app.mainloop()  # Start the Tkinter event loop

    def draw_grid(self):
        for i in range(self.size):
            for j in range(self.size):
                # Set the color based on the grid value
                color = "white" if self.grid[i][j] == 0 else "black"
                self.canvas.create_rectangle(
                    # Draw a rectangle on the canvas
                    j * 40, i * 40, (j + 1) * 40, (i + 1) * 40, fill=color)
        self.canvas.create_rectangle(
            # Draw the start position rectangle
            self.start[1] * 40, self.start[0] * 40, (self.start[1] + 1) * 40, (self.start[0] + 1) * 40, fill="green")
        self.canvas.create_rectangle(
            # Draw the end position rectangle
            self.end[1] * 40, self.end[0] * 40, (self.end[1] + 1) * 40, (self.end[0] + 1) * 40, fill="red")

    def bfs(self, start):
        queue = deque([start])  # Create a deque with the start position
        while queue:
            node = queue.popleft()  # Get the next node from the queue
            if node == self.end:  # If the node is the end position, path is found
                # Show a message box with the path found message
                messagebox.showinfo("BFS Visualizer", "Path found!")
                self.app.quit()  # Quit the application
                return
            if node in self.visited:  # If the node is already visited, skip it
                continue
            self.visited.add(node)  # Mark the node as visited
            x, y = node
            self.canvas.create_rectangle(
                # Draw a blue rectangle to represent the visited node
                y * 40, x * 40, (y + 1) * 40, (x + 1) * 40, fill="blue")
            self.app.update()  # Update the Tkinter application
            self.app.after(100)  # Delay for visualization
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # Check all four adjacent nodes
                nx, ny = x + dx, y + dy
                # If the adjacent node is within the grid and not visited, add it to the queue
                if 0 <= nx < self.size and 0 <= ny < self.size and (nx, ny) not in self.visited and self.grid[nx][ny] == 0:
                    queue.append((nx, ny))


if __name__ == "__main__":
    BFSVisualizer()
