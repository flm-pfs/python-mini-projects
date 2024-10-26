import tkinter as tk
from tkinter import messagebox, scrolledtext


class RecipeBookApp:
    def __init__(self, master):
        self.master = master
        master.title("Recipe Book")

        self.recipes = {
            "Pancakes": "Ingredients: Flour, Milk, Eggs, Sugar, Salt\nInstructions: Mix all ingredients, cook on a pan.",
            "Spaghetti": "Ingredients: Spaghetti, Tomato Sauce, Garlic, Olive Oil\nInstructions: Boil spaghetti, sauté garlic, mix with sauce.",
            "Salad": "Ingredients: Lettuce, Cucumber, Tomato, Dressing\nInstructions: Chop vegetables, mix with dressing."
        }

        self.recipe_listbox = tk.Listbox(master)
        self.recipe_listbox.pack(pady=10)
        for recipe in self.recipes:
            self.recipe_listbox.insert(tk.END, recipe)

        self.view_button = tk.Button(
            master, text="View Recipe", command=self.view_recipe)
        self.view_button.pack(pady=5)

        self.add_button = tk.Button(
            master, text="Add Recipe", command=self.add_recipe)
        self.add_button.pack(pady=5)

    def view_recipe(self):
        # Get the selected recipe from the listbox
        selected = self.recipe_listbox.get(self.recipe_listbox.curselection())
        # Show a message box with the recipe details
        messagebox.showinfo("Recipe", self.recipes[selected])

    def add_recipe(self):
        # Create a new window for adding a recipe
        add_window = tk.Toplevel(self.master)
        add_window.title("Add Recipe")

        # Recipe Name label and entry field
        tk.Label(add_window, text="Recipe Name:").grid(
            row=0, column=0, padx=10, pady=5)
        name_entry = tk.Entry(add_window)
        name_entry.grid(row=0, column=1, padx=10, pady=5)

        # Ingredients label and scrolledtext field
        tk.Label(add_window, text="Ingredients:").grid(
            row=1, column=0, padx=10, pady=5)
        ingredients_text = scrolledtext.ScrolledText(
            add_window, width=30, height=5)
        ingredients_text.grid(row=1, column=1, padx=10, pady=5)

        # Instructions label and scrolledtext field
        tk.Label(add_window, text="Instructions:").grid(
            row=2, column=0, padx=10, pady=5)
        instructions_text = scrolledtext.ScrolledText(
            add_window, width=30, height=5)
        instructions_text.grid(row=2, column=1, padx=10, pady=5)

        def save_recipe():
            # Get the values from the entry and scrolledtext fields
            name = name_entry.get()
            ingredients = ingredients_text.get("1.0", tk.END).strip()
            instructions = instructions_text.get("1.0", tk.END).strip()
            if name and ingredients and instructions:
                # Save the recipe in the recipes dictionary
                self.recipes[name] = f"Ingredients: {
                    ingredients}\nInstructions: {instructions}"
                # Add the recipe to the listbox
                self.recipe_listbox.insert(tk.END, name)
                # Close the add window
                add_window.destroy()
            else:
                # Show a warning message if any field is empty
                messagebox.showwarning(
                    "Input Error", "All fields must be filled out.")

        # Save button
        save_button = tk.Button(add_window, text="Save", command=save_recipe)
        save_button.grid(row=3, column=0, columnspan=2, pady=10)


if __name__ == "__main__":
    # Create the main window
    root = tk.Tk()
    # Create an instance of the RecipeBookApp class
    app = RecipeBookApp(root)
    # Start the main event loop
    root.mainloop()
