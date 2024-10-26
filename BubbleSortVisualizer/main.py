import tkinter as tk
import random


class BubbleSortVisualizer:
    def __init__(self, master):
        self.master = master
        self.master.title("Bubble Sort Visualizer")
        self.master.geometry("800x600")
        self.canvas = tk.Canvas(self.master, width=800, height=500)
        self.canvas.pack()
        self.frame = tk.Frame(self.master)
        self.frame.pack(pady=20)
        self.start_button = tk.Button(
            self.frame, text="Start Sorting", command=self.start_sorting)
        self.start_button.pack(side=tk.LEFT)
        self.pause_button = tk.Button(
            self.frame, text="Pause", command=self.pause_sorting)
        self.pause_button.pack(side=tk.LEFT, padx=10)
        self.reset_button = tk.Button(
            self.frame, text="Reset", command=self.reset)
        self.reset_button.pack(side=tk.LEFT, padx=10)
        self.array = [random.randint(10, 400) for _ in range(100)]
        self.draw_array()
        self.sorting = False
        self.paused = False

    def draw_array(self):
        # Clear the canvas
        self.canvas.delete("all")
        array_width = 800 / len(self.array)
        for i, height in enumerate(self.array):
            x0 = i * array_width
            y0 = 500
            x1 = x0 + array_width
            y1 = 500 - height
            # Draw a rectangle representing the array element
            self.canvas.create_rectangle(x0, y0, x1, y1, fill="blue")
        self.master.update()

    def start_sorting(self):
        if not self.sorting:
            self.sorting = True
            self.sort_step()

    def sort_step(self):
        if self.paused:
            return
        n = len(self.array)
        for i in range(n):
            for j in range(0, n-i-1):
                if self.array[j] > self.array[j+1]:
                    # Swap the elements if they are in the wrong order
                    self.array[j], self.array[j +
                                              1] = self.array[j+1], self.array[j]
                    self.draw_array()
                    self.master.after(10, self.sort_step)
                    return
        self.sorting = False

    def pause_sorting(self):
        self.paused = not self.paused
        if self.paused:
            self.pause_button.config(text="Play")
        else:
            self.pause_button.config(text="Pause")
            if self.sorting:
                self.sort_step()

    def reset(self):
        self.sorting = False
        self.paused = False
        self.pause_button.config(text="Pause")
        self.array = [random.randint(10, 400) for _ in range(100)]
        self.draw_array()


if __name__ == "__main__":
    root = tk.Tk()
    app = BubbleSortVisualizer(root)
    root.mainloop()
