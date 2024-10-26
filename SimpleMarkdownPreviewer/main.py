import tkinter as tk
from tkinter import scrolledtext
import markdown

class MarkdownPreviewer:
    def __init__(self, root):
        self.root = root
        self.root.title("Markdown Previewer")
        self.root.geometry("800x600")

        self.editor_frame = tk.Frame(self.root)
        self.editor_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.preview_frame = tk.Frame(self.root)
        self.preview_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.editor = scrolledtext.ScrolledText(self.editor_frame, wrap=tk.WORD)
        self.editor.pack(fill=tk.BOTH, expand=True)
        self.editor.bind("<KeyRelease>", self.update_preview)

        self.preview = tk.Text(self.preview_frame, wrap=tk.WORD, state=tk.DISABLED)
        self.preview.pack(fill=tk.BOTH, expand=True)

    def update_preview(self, event=None):
        markdown_text = self.editor.get(1.0, tk.END)
        html_text = markdown.markdown(markdown_text)
        self.preview.config(state=tk.NORMAL)
        self.preview.delete(1.0, tk.END)
        self.preview.insert(tk.END, html_text)
        self.preview.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = MarkdownPreviewer(root)
    root.mainloop()