import tkinter as tk
from tkinter import colorchooser, messagebox


class DrawingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Drawing Application")
        self.root.geometry("800x600")

        self.canvas = tk.Canvas(root, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.pen_color = "black"
        self.bg_color = "white"
        self.pen_size = 5
        self.drawing = False
        self.eraser_mode = False

        self.create_menu()
        self.canvas.bind("<Button-1>", self.start_drawing)
        self.canvas.bind("<ButtonRelease-1>", self.stop_drawing)
        self.canvas.bind("<B1-Motion>", self.draw)

    def create_menu(self):
        # Create the menu bar
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)

        # Create the File menu
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Clear Canvas", command=self.clear_canvas)
        file_menu.add_command(label="Exit", command=self.root.quit)

        # Create the Color menu
        color_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Color", menu=color_menu)
        color_menu.add_command(label="Choose Pen Color",
                               command=self.choose_pen_color)
        color_menu.add_command(
            label="Choose Background Color", command=self.choose_bg_color)

        # Create the Tools menu
        tool_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Tools", menu=tool_menu)
        tool_menu.add_command(label="Eraser", command=self.toggle_eraser)

    def start_drawing(self, event):
        # Start drawing when the left mouse button is pressed
        self.drawing = True
        self.last_x, self.last_y = event.x, event.y

    def stop_drawing(self, event):
        # Stop drawing when the left mouse button is released
        self.drawing = False

    def draw(self, event):
        # Draw lines or erase based on the current mode
        if self.drawing:
            x, y = event.x, event.y
            if self.eraser_mode:
                eraser_size = self.pen_size * 2  # Increase the eraser size
                self.canvas.create_rectangle(x - eraser_size, y - eraser_size, x +
                                             eraser_size, y + eraser_size, fill=self.bg_color, outline=self.bg_color)
            else:
                self.canvas.create_line(self.last_x, self.last_y, x, y, width=self.pen_size,
                                        fill=self.pen_color, capstyle=tk.ROUND, smooth=True)
            self.last_x, self.last_y = x, y

    def clear_canvas(self):
        # Clear the canvas by deleting all items
        self.canvas.delete("all")

    def choose_pen_color(self):
        # Open a color chooser dialog to choose the pen color
        color_code = colorchooser.askcolor(title="Choose pen color")
        if color_code[1]:
            self.pen_color = color_code[1]

    def choose_bg_color(self):
        # Open a color chooser dialog to choose the background color
        color_code = colorchooser.askcolor(title="Choose background color")
        if color_code[1]:
            self.bg_color = color_code[1]
            self.canvas.config(bg=self.bg_color)

    def toggle_eraser(self):
        # Toggle the eraser mode and change the cursor accordingly
        self.eraser_mode = not self.eraser_mode
        if self.eraser_mode:
            self.root.config(cursor="cross")
        else:
            self.root.config(cursor="")


if __name__ == "__main__":
    root = tk.Tk()
    app = DrawingApp(root)
    root.mainloop()
