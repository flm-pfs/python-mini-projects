import tkinter as tk


class DrawingApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Drawing App")
        self.master.geometry("800x600")

        self.canvas = tk.Canvas(self.master, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.canvas.bind("<Button-1>", self.start_drawing)
        self.canvas.bind("<B1-Motion>", self.draw)
        self.canvas.bind("<ButtonRelease-1>", self.stop_drawing)

        self.drawing = False
        self.last_x = 0
        self.last_y = 0

    def start_drawing(self, event):
        # Set drawing flag to True and store initial coordinates
        self.drawing = True
        self.last_x, self.last_y = event.x, event.y

    def draw(self, event):
        if self.drawing:
            x, y = event.x, event.y
            # Draw a line from last coordinates to current coordinates
            self.canvas.create_line(
                self.last_x, self.last_y, x, y, fill="black", width=2)
            self.last_x, self.last_y = x, y

    def stop_drawing(self, event):
        # Set drawing flag to False when mouse button is released
        self.drawing = False


def main():
    root = tk.Tk()
    app = DrawingApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
