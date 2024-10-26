import time
import tkinter as tk
from tkinter import messagebox


class PomodoroTimer:
    def __init__(self, master):
        self.master = master
        master.title("Pomodoro Timer")

        self.timer_label = tk.Label(
            master, text="25:00", font=("Helvetica", 48))
        self.timer_label.pack(pady=20)

        self.start_button = tk.Button(
            master, text="Start", command=self.start_timer)
        self.start_button.pack(side=tk.LEFT, padx=10)

        self.pause_button = tk.Button(
            master, text="Pause", command=self.pause_timer, state=tk.DISABLED)
        self.pause_button.pack(side=tk.LEFT, padx=10)

        self.reset_button = tk.Button(
            master, text="Reset", command=self.reset_timer)
        self.reset_button.pack(side=tk.LEFT, padx=10)

        self.time_left = 1500  # 25 minutes in seconds
        self.running = False

    def start_timer(self):
        """
        Starts the timer and disables the start button.
        """
        self.running = True
        self.start_button.config(state=tk.DISABLED)
        self.pause_button.config(state=tk.NORMAL)
        self.countdown()

    def pause_timer(self):
        """
        Pauses the timer and enables the start button.
        """
        self.running = False
        self.start_button.config(state=tk.NORMAL)
        self.pause_button.config(state=tk.DISABLED)

    def reset_timer(self):
        """
        Resets the timer to the initial state.
        """
        self.running = False
        self.time_left = 1500
        self.update_label()
        self.start_button.config(state=tk.NORMAL)
        self.pause_button.config(state=tk.DISABLED)

    def countdown(self):
        """
        Updates the timer label every second until the time is up.
        """
        if self.running and self.time_left > 0:
            minutes, seconds = divmod(self.time_left, 60)
            self.update_label(minutes, seconds)
            self.time_left -= 1
            self.master.after(1000, self.countdown)
        elif self.time_left == 0:
            self.running = False
            self.update_label()
            messagebox.showinfo("Pomodoro Timer", "Time's up!")
            self.reset_timer()

    def update_label(self, minutes=25, seconds=0):
        """
        Updates the timer label with the specified minutes and seconds.
        """
        self.timer_label.config(text=f"{minutes:02d}:{seconds:02d}")


if __name__ == "__main__":
    root = tk.Tk()
    app = PomodoroTimer(root)
    root.mainloop()
