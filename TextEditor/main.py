import tkinter as tk
from tkinter import filedialog


class TextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Text Editor")
        self.root.geometry("800x600")

        self.text_area = tk.Text(self.root, wrap='word')
        self.text_area.pack(expand=1, fill='both')

        self.menu_bar = tk.Menu(self.root)
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.root.quit)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)

        self.root.config(menu=self.menu_bar)

    def open_file(self):
        # Open a file dialog to select a file
        file_path = filedialog.askopenfilename(
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            # If a file is selected, open it and read its contents
            with open(file_path, 'r') as file:
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.END, file.read())

    def save_file(self):
        # Open a file dialog to select a file to save
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[
            ("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            # If a file is selected, save the contents of the text area to the file
            with open(file_path, 'w') as file:
                file.write(self.text_area.get(1.0, tk.END))


if __name__ == "__main__":
    # Create a Tkinter root window
    root = tk.Tk()
    # Create an instance of the TextEditor class
    text_editor = TextEditor(root)
    # Start the Tkinter event loop
    root.mainloop()
