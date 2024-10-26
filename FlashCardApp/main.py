import tkinter as tk
from tkinter import messagebox


class FlashcardApp:
    def __init__(self, master):
        self.master = master
        master.title("Flashcard App")

        # Define the flashcards
        self.flashcards = [
            {"question": "What is the capital of France?", "answer": "Paris"},
            {"question": "What is 2 + 2?", "answer": "4"},
            {"question": "What is the largest planet?", "answer": "Jupiter"}
        ]
        self.current_card = 0

        # Create the question label
        self.question_label = tk.Label(master, text="", font=("Helvetica", 24))
        self.question_label.pack(pady=20)

        # Create the answer button
        self.answer_button = tk.Button(
            master, text="Show Answer", command=self.show_answer)
        self.answer_button.pack(pady=10)

        # Create the next button
        self.next_button = tk.Button(
            master, text="Next Card", command=self.next_card)
        self.next_button.pack(pady=10)

        # Show the first question
        self.show_question()

    def show_question(self):
        if self.current_card < len(self.flashcards):
            # Display the current question
            self.question_label.config(
                text=self.flashcards[self.current_card]["question"])
        else:
            # Show a message when there are no more flashcards
            messagebox.showinfo("Flashcard App", "No more flashcards!")

    def show_answer(self):
        # Display the answer for the current flashcard
        messagebox.showinfo(
            "Answer", self.flashcards[self.current_card]["answer"])

    def next_card(self):
        # Move to the next flashcard
        self.current_card += 1
        if self.current_card < len(self.flashcards):
            # Show the next question
            self.show_question()
        else:
            # Show a message when there are no more flashcards
            messagebox.showinfo("Flashcard App", "No more flashcards!")
            root.quit()


if __name__ == "__main__":
    # Create the root window
    root = tk.Tk()

    # Create an instance of the FlashcardApp
    app = FlashcardApp(root)

    # Start the main event loop
    root.mainloop()
