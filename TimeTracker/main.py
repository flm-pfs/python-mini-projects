import tkinter as tk
from tkinter import ttk
import time


class TimeTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Time Tracker")
        self.root.geometry("300x200")

        self.elapsed_time = 0
        self.running = False
        self.start_time = None

        self.create_widgets()
        self.update_time()

    def create_widgets(self):
        # Create a label to display the time
        self.time_label = ttk.Label(
            self.root, text="00:00:00", font=("Helvetica", 40))
        self.time_label.pack(pady=20)

        # Create buttons for starting, stopping, and resetting the timer
        self.start_button = ttk.Button(
            self.root, text="Start", command=self.start_timer)
        self.start_button.pack(side=tk.LEFT, padx=10)

        self.stop_button = ttk.Button(
            self.root, text="Stop", command=self.stop_timer)
        self.stop_button.pack(side=tk.LEFT, padx=10)

        self.reset_button = ttk.Button(
            self.root, text="Reset", command=self.reset_timer)
        self.reset_button.pack(side=tk.LEFT, padx=10)

    def start_timer(self):
        # Start the timer if it's not already running
        if not self.running:
            self.running = True
            self.start_time = time.time() - self.elapsed_time
            self.update_time()

    def stop_timer(self):
        # Stop the timer if it's running
        if self.running:
            self.running = False

    def reset_timer(self):
        # Reset the timer to 0
        self.running = False
        self.elapsed_time = 0
        self.time_label.config(text="00:00:00")

    def update_time(self):
        # Update the time label every second if the timer is running
        if self.running:
            self.elapsed_time = time.time() - self.start_time
            self.time_label.config(text=self.format_time(self.elapsed_time))
        self.root.after(1000, self.update_time)

    def format_time(self, elapsed_time):
        # Format the elapsed time into HH:MM:SS format
        hours = int(elapsed_time // 3600)
        minutes = int((elapsed_time % 3600) // 60)
        seconds = int(elapsed_time % 60)
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"


if __name__ == "__main__":
    root = tk.Tk()
    app = TimeTracker(root)
    root.mainloop()
