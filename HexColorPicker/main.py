import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pyperclip


class HexColorPickerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hex Color Picker")
        self.red = tk.IntVar(value=0)
        self.green = tk.IntVar(value=0)
        self.blue = tk.IntVar(value=0)
        self.create_widgets()

    def create_widgets(self):
        # Create a frame to hold the widgets
        frame = ttk.Frame(self.root, padding="10")
        frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Create a label and scale for the red color component
        ttk.Label(frame, text="Red:").grid(
            row=0, column=0, sticky=tk.W, pady=5)
        red_scale = ttk.Scale(frame, from_=255, to=0,
                              variable=self.red, command=self.update_color)
        red_scale.grid(row=0, column=1, sticky=tk.W, pady=5)

        # Create a label and scale for the green color component
        ttk.Label(frame, text="Green:").grid(
            row=1, column=0, sticky=tk.W, pady=5)
        green_scale = ttk.Scale(frame, from_=255, to=0,
                                variable=self.green, command=self.update_color)
        green_scale.grid(row=1, column=1, sticky=tk.W, pady=5)

        # Create a label and scale for the blue color component
        ttk.Label(frame, text="Blue:").grid(
            row=2, column=0, sticky=tk.W, pady=5)
        blue_scale = ttk.Scale(frame, from_=255, to=0,
                               variable=self.blue, command=self.update_color)
        blue_scale.grid(row=2, column=1, sticky=tk.W, pady=5)

        # Create a label to display the selected color
        self.color_label = ttk.Label(
            frame, text="#000000", background="#000000", padding=(20, 10))
        self.color_label.grid(row=3, column=0, columnspan=2, pady=10)

        # Create a button to copy the color to clipboard
        copy_button = ttk.Button(
            frame, text="Copy", command=self.copy_to_clipboard)
        copy_button.grid(row=4, column=0, columnspan=2, pady=10)

    def update_color(self, *args):
        # Get the values of red, green, and blue color components
        red = self.red.get()
        green = self.green.get()
        blue = self.blue.get()

        # Convert the color components to hexadecimal format
        hex_color = f"#{red:02x}{green:02x}{blue:02x}"

        # Update the color label with the selected color
        self.color_label.config(text=hex_color, background=hex_color)

    def copy_to_clipboard(self):
        # Get the hexadecimal color from the color label
        hex_color = self.color_label.cget("text")

        # Copy the color to clipboard
        pyperclip.copy(hex_color)

        # Show a message box to indicate that the color has been copied
        messagebox.showinfo("Copied", f"Hex color {
                            hex_color} copied to clipboard")


if __name__ == "__main__":
    # Create the root window
    root = tk.Tk()

    # Create an instance of the HexColorPickerApp
    app = HexColorPickerApp(root)

    # Start the main event loop
    root.mainloop()
