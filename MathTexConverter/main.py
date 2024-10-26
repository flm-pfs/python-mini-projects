import tkinter as tk
from tkinter import messagebox
from latex2mathml.converter import convert


def convert_text():
    latex_input = entry.get()
    try:
        mathml_output = convert(latex_input)
        output_text.config(state=tk.NORMAL)
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, mathml_output)
        output_text.config(state=tk.DISABLED)
    except Exception as e:
        messagebox.showerror("Conversion Error", str(e))


# Create the main window
root = tk.Tk()
root.title("Tex to Formula Converter")

# Create and place the input label and entry widget
input_label = tk.Label(root, text="Enter LaTeX:")
input_label.pack(pady=10)

entry = tk.Entry(root, width=50)
entry.pack(pady=10)

# Create and place the convert button
convert_button = tk.Button(root, text="Convert", command=convert_text)
convert_button.pack(pady=10)

# Create and place the output text widget
output_text = tk.Text(root, width=50, height=10, state=tk.DISABLED)
output_text.pack(pady=10)

# Run the application
root.mainloop()
