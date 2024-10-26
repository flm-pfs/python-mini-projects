import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def quadratic_equation_solver(a, b, c):
    """
    Solves the quadratic equation ax^2 + bx + c = 0
    :param a: coefficient of x^2
    :param b: coefficient of x
    :param c: constant term
    :return: tuple of real roots or None if no real roots
    """
    # Calculate the discriminant
    discriminant = b**2 - 4*a*c

    # Check if the discriminant is negative (no real roots)
    if discriminant < 0:
        return None

    # Calculate the two roots
    sqrt_discriminant = np.sqrt(discriminant)
    root1 = (-b + sqrt_discriminant) / (2*a)
    root2 = (-b - sqrt_discriminant) / (2*a)

    return (root1, root2)


def plot_quadratic_equation(a, b, c, canvas):
    """
    Plots the quadratic equation ax^2 + bx + c = 0 on the given canvas
    :param a: coefficient of x^2
    :param b: coefficient of x
    :param c: constant term
    :param canvas: tkinter canvas to draw the plot on
    """
    # Clear previous plot
    for widget in canvas.winfo_children():
        widget.destroy()

    # Create a figure and axis
    fig, ax = plt.subplots(figsize=(5, 4), dpi=100)

    # Generate x values
    x = np.linspace(-10, 10, 400)

    # Calculate y values
    y = a*x**2 + b*x + c

    # Plot the quadratic equation
    ax.plot(x, y, label=f'{a}x^2 + {b}x + {c}')

    # Plot the roots if they exist
    roots = quadratic_equation_solver(a, b, c)
    if roots:
        ax.scatter(roots, [0, 0], color='red', label='Roots')

    # Add labels and title
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('Quadratic Equation')
    ax.legend()
    ax.grid(True)
    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)

    # Embed the plot in the tkinter canvas
    canvas_widget = FigureCanvasTkAgg(fig, master=canvas)
    canvas_widget.draw()
    canvas_widget.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)


def create_gui():
    """
    Creates the tkinter GUI for the quadratic equation visualizer
    """
    root = tk.Tk()
    root.title("Quadratic Equation Visualizer")

    # Create input fields
    tk.Label(root, text="a:").grid(row=0, column=0)
    a_entry = tk.Entry(root)
    a_entry.grid(row=0, column=1)

    tk.Label(root, text="b:").grid(row=1, column=0)
    b_entry = tk.Entry(root)
    b_entry.grid(row=1, column=1)

    tk.Label(root, text="c:").grid(row=2, column=0)
    c_entry = tk.Entry(root)
    c_entry.grid(row=2, column=1)

    # Create a canvas for the plot
    canvas = tk.Canvas(root)
    canvas.grid(row=3, column=0, columnspan=2)

    # Create a button to plot the equation
    def plot_button_click():
        a = float(a_entry.get())
        b = float(b_entry.get())
        c = float(c_entry.get())
        plot_quadratic_equation(a, b, c, canvas)

    plot_button = tk.Button(root, text="Plot", command=plot_button_click)
    plot_button.grid(row=4, column=0, columnspan=2)

    # Create an exit button
    exit_button = tk.Button(root, text="Exit", command=root.quit)
    exit_button.grid(row=5, column=0, columnspan=2)

    root.mainloop()


# Create the GUI
create_gui()
