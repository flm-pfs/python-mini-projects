import tkinter as tk


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Basic Calculator")

        # Create an entry widget for displaying the input and result
        self.entry = tk.Entry(self.root, width=20, font=('Arial', 16))
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        row = 1
        col = 0
        for button in buttons:
            # Create a button for each element in the buttons list
            tk.Button(self.root, text=button, width=5, height=2,
                      command=lambda b=button: self.on_button_click(b)).grid(row=row, column=col)
            col += 1
            if col > 3:
                col = 0
                row += 1

        # Create a clear button
        tk.Button(self.root, text='C', width=5, height=2,
                  command=self.clear).grid(row=row, column=col)

    def on_button_click(self, button):
        if button == '=':
            try:
                # Evaluate the expression and display the result
                result = eval(self.entry.get())
                self.entry.delete(0, tk.END)
                self.entry.insert(0, result)
            except Exception as e:
                # Display "Error" if there is an exception during evaluation
                self.entry.delete(0, tk.END)
                self.entry.insert(0, "Error")
        elif button == 'C':
            # Clear the entry widget
            self.clear()
        else:
            # Append the button value to the entry widget
            self.entry.insert(tk.END, button)

    def clear(self):
        # Clear the entry widget
        self.entry.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()
