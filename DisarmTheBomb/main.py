import tkinter as tk
import time
import random


class BombDisarmGame:
    def __init__(self, master):
        # Initialize the main window
        self.master = master
        self.master.title("Disarm the Bomb")
        self.master.geometry("600x200")

        # Define the wires and initialize lists to track cut wires and their order
        self.wires = ["red", "blue", "green"]
        self.cut_wires = []
        self.wire_order = random.sample(self.wires, len(
            self.wires))  # Random order of wires to cut
        # Random time limit between 5 to 10 seconds
        self.time_limit = random.randint(5, 10)
        self.start_time = None

        # Create and pack the main label
        self.label = tk.Label(
            master, text="Cut the wires in the correct order to disarm the bomb!", font=("Helvetica", 14))
        self.label.pack(pady=20)

        # Create and pack wire labels, and bind click events to cut_wire method
        self.wire_labels = {}
        for wire in self.wires:
            wire_label = tk.Label(master, text=f"{wire.capitalize()} Wire", font=(
                "Helvetica", 12), bg=wire, fg="white")
            wire_label.pack(fill=tk.X, padx=20)
            wire_label.bind("<Button-1>", lambda event,
                            w=wire: self.cut_wire(w))
            self.wire_labels[wire] = wire_label

        # Create and pack the timer label
        self.timer_label = tk.Label(
            master, text="Time left: 0", font=("Helvetica", 12))
        self.timer_label.pack(pady=20)

        # Start the game
        self.start_game()

    def start_game(self):
        # Set the start time and begin updating the timer
        self.start_time = time.time()
        self.update_timer()

    def update_timer(self):
        # Update the timer label every second
        if self.start_time is not None:
            elapsed_time = time.time() - self.start_time
            time_left = max(0, self.time_limit - elapsed_time)
            self.timer_label.config(text=f"Time left: {int(time_left)}")
            if time_left > 0:
                self.master.after(1000, self.update_timer)
            else:
                self.game_over(False)

    def cut_wire(self, wire):
        # Handle wire cutting logic
        if self.start_time is not None and wire not in self.cut_wires:
            self.cut_wires.append(wire)
            self.wire_labels[wire].config(
                text=f"{wire.capitalize()} Wire (Cut)", fg="black")
            if self.cut_wires == self.wire_order:
                self.game_over(True)
            elif self.cut_wires[-1] != self.wire_order[len(self.cut_wires) - 1]:
                self.game_over(False)

    def game_over(self, win):
        # Handle game over logic, update the main label, and unbind wire clicks
        self.start_time = None  # Stop the timer
        if win:
            self.label.config(
                text="Congratulations! You disarmed the bomb!", fg="green")
        else:
            self.label.config(
                text="Boom! You failed to disarm the bomb.", fg="red")
        for wire in self.wires:
            self.wire_labels[wire].unbind("<Button-1>")


if __name__ == "__main__":
    root = tk.Tk()
    game = BombDisarmGame(root)
    root.mainloop()
