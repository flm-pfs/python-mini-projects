import tkinter as tk
from tkinter import ttk


class LogicGateVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Logic Gate Simulator")

        # Variables to store the selected gate, input values, and output value
        self.gate_var = tk.StringVar()
        self.input1_var = tk.IntVar()
        self.input2_var = tk.IntVar()
        self.output_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        frame = ttk.Frame(self.root, padding="10")
        frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Gate selection
        ttk.Label(frame, text="Select Gate:").grid(
            row=0, column=0, sticky=tk.W, pady=5)
        gate_choices = ["AND", "OR", "NOT"]
        gate_menu = ttk.OptionMenu(
            frame, self.gate_var, gate_choices[0], *gate_choices, command=self.update_output)
        gate_menu.grid(row=0, column=1, sticky=tk.W, pady=5)

        # Input 1
        ttk.Label(frame, text="Input 1:").grid(
            row=1, column=0, sticky=tk.W, pady=5)
        input1_spinbox = ttk.Spinbox(
            frame, from_=0, to=1, textvariable=self.input1_var, command=self.update_output)
        input1_spinbox.grid(row=1, column=1, sticky=tk.W, pady=5)

        # Input 2 (only for AND and OR)
        ttk.Label(frame, text="Input 2:").grid(
            row=2, column=0, sticky=tk.W, pady=5)
        input2_spinbox = ttk.Spinbox(
            frame, from_=0, to=1, textvariable=self.input2_var, command=self.update_output)
        input2_spinbox.grid(row=2, column=1, sticky=tk.W, pady=5)

        # Output
        ttk.Label(frame, text="Output:").grid(
            row=3, column=0, sticky=tk.W, pady=5)
        output_label = ttk.Label(
            frame, textvariable=self.output_var, font=("Helvetica", 14, "bold"))
        output_label.grid(row=3, column=1, sticky=tk.W, pady=5)

    def update_output(self, *args):
        # Get the selected gate and input values
        gate = self.gate_var.get()
        input1 = self.input1_var.get()
        input2 = self.input2_var.get() if gate != "NOT" else None

        # Perform the logic gate operation based on the selected gate
        if gate == "AND":
            result = input1 & input2
        elif gate == "OR":
            result = input1 | input2
        elif gate == "NOT":
            result = 1 - input1

        # Update the output value
        self.output_var.set(str(result))


if __name__ == "__main__":
    # Create the root window and start the application
    root = tk.Tk()
    app = LogicGateVisualizer(root)
    root.mainloop()
