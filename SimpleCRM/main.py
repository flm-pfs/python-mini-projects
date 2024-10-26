import tkinter as tk
from tkinter import ttk
import sqlite3


class SimpleCRM:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple CRM")
        self.root.geometry("1000x500")

        self.conn = sqlite3.connect('SimpleCRM/crm.db')
        self.create_table()

        self.create_widgets()

    def create_table(self):
        # Create a table in the database if it doesn't exist
        cursor = self.conn.cursor()
        cursor.execute('''
			CREATE TABLE IF NOT EXISTS customers (
				id INTEGER PRIMARY KEY AUTOINCREMENT,
				name TEXT NOT NULL,
				email TEXT NOT NULL,
				phone TEXT NOT NULL
			)
		''')
        self.conn.commit()

    def create_widgets(self):
        # Create labels and entry fields for name, email, and phone
        self.name_label = ttk.Label(self.root, text="Name:")
        self.name_label.grid(row=0, column=0, padx=10, pady=10)
        self.name_entry = ttk.Entry(self.root, width=30)
        self.name_entry.grid(row=0, column=1, padx=10, pady=10)

        self.email_label = ttk.Label(self.root, text="Email:")
        self.email_label.grid(row=1, column=0, padx=10, pady=10)
        self.email_entry = ttk.Entry(self.root, width=30)
        self.email_entry.grid(row=1, column=1, padx=10, pady=10)

        self.phone_label = ttk.Label(self.root, text="Phone:")
        self.phone_label.grid(row=2, column=0, padx=10, pady=10)
        self.phone_entry = ttk.Entry(self.root, width=30)
        self.phone_entry.grid(row=2, column=1, padx=10, pady=10)

        # Create a button to add a customer
        self.add_button = ttk.Button(
            self.root, text="Add Customer", command=self.add_customer)
        self.add_button.grid(row=3, column=0, columnspan=2, pady=10)

        # Create a treeview to display customer data
        self.tree = ttk.Treeview(self.root, columns=(
            "ID", "Name", "Email", "Phone"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Email", text="Email")
        self.tree.heading("Phone", text="Phone")
        self.tree.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        # Create a button to delete a customer
        self.delete_button = ttk.Button(
            self.root, text="Delete Customer", command=self.delete_customer)
        self.delete_button.grid(row=5, column=0, columnspan=2, pady=10)

        # Load existing customers
        self.load_customers()

    def add_customer(self):
        # Get customer details from entry fields
        name = self.name_entry.get()
        email = self.email_entry.get()
        phone = self.phone_entry.get()

        # Insert customer data into the database
        cursor = self.conn.cursor()
        cursor.execute('''
			INSERT INTO customers (name, email, phone) VALUES (?, ?, ?)
		''', (name, email, phone))
        self.conn.commit()

        # Clear entry fields
        self.name_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)

        # Reload customer data
        self.load_customers()

    def delete_customer(self):
        # Get the selected customer from the treeview
        selected_item = self.tree.selection()[0]
        customer_id = self.tree.item(selected_item)['values'][0]

        # Delete the customer from the database
        cursor = self.conn.cursor()
        cursor.execute('''
			DELETE FROM customers WHERE id = ?
		''', (customer_id,))
        self.conn.commit()

        # Reload customer data
        self.load_customers()

    def load_customers(self):
        # Clear the treeview
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Fetch all customers from the database
        cursor = self.conn.cursor()
        cursor.execute('''
			SELECT * FROM customers
		''')
        customers = cursor.fetchall()

        # Insert customers into the treeview
        for customer in customers:
            self.tree.insert("", tk.END, values=customer)


if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleCRM(root)
    root.mainloop()
