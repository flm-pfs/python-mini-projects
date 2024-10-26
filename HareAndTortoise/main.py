import tkinter as tk
import time
import random

# Constants for the race
WIDTH = 800
HEIGHT = 200
START_LINE = 50
FINISH_LINE = WIDTH - 50

# Create the main window
root = tk.Tk()
root.title("Hare and Tortoise Race")

# Create a canvas to draw the race
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)
canvas.pack()

# Draw the start and finish lines
canvas.create_line(START_LINE, 0, START_LINE, HEIGHT, fill="green", width=2)
canvas.create_line(FINISH_LINE, 0, FINISH_LINE, HEIGHT, fill="red", width=2)

# Create the Hare and Tortoise
hare = canvas.create_oval(START_LINE, 50, START_LINE + 20, 70, fill="brown")
tortoise = canvas.create_oval(
    START_LINE, 150, START_LINE + 20, 170, fill="green")

# Labels for the Hare and Tortoise
hare_label = canvas.create_text(START_LINE + 30, 60, text="Hare", fill="brown")
tortoise_label = canvas.create_text(
    START_LINE + 30, 160, text="Tortoise", fill="green")

# Function to move the Hare and Tortoise


def move_animals():
    hare_pos = START_LINE
    tortoise_pos = START_LINE

    while hare_pos < FINISH_LINE and tortoise_pos < FINISH_LINE:
        # Move the Hare
        hare_step = random.randint(1, 10)
        hare_pos += hare_step
        canvas.move(hare, hare_step, 0)
        canvas.move(hare_label, hare_step, 0)

        # Move the Tortoise
        tortoise_step = random.randint(1, 5)
        tortoise_pos += tortoise_step
        canvas.move(tortoise, tortoise_step, 0)
        canvas.move(tortoise_label, tortoise_step, 0)

        # Update the canvas
        canvas.update()
        time.sleep(0.1)

    # Determine the winner
    if hare_pos >= FINISH_LINE and tortoise_pos >= FINISH_LINE:
        winner = "It's a tie!"
    elif hare_pos >= FINISH_LINE:
        winner = "Hare wins!"
    else:
        winner = "Tortoise wins!"

    # Display the winner
    canvas.create_text(WIDTH // 2, HEIGHT // 2, text=winner,
                       font=("Arial", 20), fill="blue")


# Start the race
move_animals()

# Run the Tkinter event loop
root.mainloop()
