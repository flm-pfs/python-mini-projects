import tkinter as tk
from tkinter import messagebox
import time
import random

# List of sentences for the typing test
sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "Python is a high-level programming language.",
    "Tkinter is a standard GUI library for Python.",
    "Practice makes perfect in typing speed.",
    "A journey of a thousand miles begins with a single step."
]


class TypingTestApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Test")

        self.sentence = random.choice(sentences)
        self.start_time = None

        # Label to display the sentence for typing
        self.label = tk.Label(root, text=self.sentence, font=("Helvetica", 16))
        self.label.pack(pady=20)

        # Entry field for user input
        self.entry = tk.Entry(root, font=("Helvetica", 16), width=50)
        self.entry.pack(pady=20)
        self.entry.bind('<Return>', self.check_typing_speed)

        # Button to start the typing test
        self.start_button = tk.Button(
            root, text="Start", command=self.start_typing_test)
        self.start_button.pack(pady=20)

    def start_typing_test(self):
        # Start the timer and set focus to the entry field
        self.start_time = time.time()
        self.entry.focus_set()
        self.start_button.config(state=tk.DISABLED)

    def check_typing_speed(self, event):
        # Get user input and calculate elapsed time
        user_input = self.entry.get()
        end_time = time.time()
        elapsed_time = end_time - self.start_time

        if user_input == self.sentence:
            # Calculate words per minute and show result
            words_per_minute = len(self.sentence.split()) / (elapsed_time / 60)
            messagebox.showinfo("Result", f"Correct! Your typing speed: {
                                words_per_minute:.2f} WPM")
        else:
            # Show incorrect result message
            messagebox.showinfo("Result", "Incorrect. Please try again.")

        # Reset the test
        self.reset_test()

    def reset_test(self):
        # Choose a new random sentence, update label and clear entry field
        self.sentence = random.choice(sentences)
        self.label.config(text=self.sentence)
        self.entry.delete(0, tk.END)
        self.start_button.config(state=tk.NORMAL)
        self.start_time = None


if __name__ == "__main__":
    # Create the main window and start the application
    root = tk.Tk()
    app = TypingTestApp(root)
    root.mainloop()
