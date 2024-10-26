import tkinter as tk
from tkinter import ttk


class UnitConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Unit Converter")
        self.root.geometry("400x200")

        self.units = {
            "Meters": 1,
            "Feet": 3.28084,
            "Kilometers": 0.001,
            "Miles": 0.000621371
        }

        self.from_unit = tk.StringVar()
        self.to_unit = tk.StringVar()
        self.from_unit.set("Meters")
        self.to_unit.set("Feet")

        self.create_widgets()

    def create_widgets(self):
        # Labels and input fields for "From" unit
        ttk.Label(self.root, text="From:").grid(
            row=0, column=0, padx=10, pady=10)
        self.from_entry = ttk.Entry(self.root, width=10)
        self.from_entry.grid(row=0, column=1, padx=10, pady=10)
        self.from_menu = ttk.Combobox(
            self.root, textvariable=self.from_unit, values=list(self.units.keys()))
        self.from_menu.grid(row=0, column=2, padx=10, pady=10)

        # Labels and input fields for "To" unit
        ttk.Label(self.root, text="To:").grid(
            row=1, column=0, padx=10, pady=10)
        self.to_entry = ttk.Entry(self.root, width=10)
        self.to_entry.grid(row=1, column=1, padx=10, pady=10)
        self.to_menu = ttk.Combobox(
            self.root, textvariable=self.to_unit, values=list(self.units.keys()))
        self.to_menu.grid(row=1, column=2, padx=10, pady=10)

        # Convert button
        ttk.Button(self.root, text="Convert", command=self.convert).grid(
            row=2, column=1, padx=10, pady=10)

    def convert(self):
        try:
            # Get input values
            from_value = float(self.from_entry.get())
            from_unit = self.from_unit.get()
            to_unit = self.to_unit.get()

            # Get conversion factors
            from_factor = self.units[from_unit]
            to_factor = self.units[to_unit]

            # Perform conversion
            result = from_value * (from_factor / to_factor)

            # Update the "To" entry field with the result
            self.to_entry.delete(0, tk.END)
            self.to_entry.insert(0, f"{result:.4f}")
        except ValueError:
            # Handle invalid input
            self.to_entry.delete(0, tk.END)
            self.to_entry.insert(0, "Invalid input")


if __name__ == "__main__":
    root = tk.Tk()
    app = UnitConverter(root)
    root.mainloop()
