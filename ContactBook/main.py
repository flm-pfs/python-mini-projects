import json


class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email):
        # Create a dictionary representing a contact
        contact = {
            "name": name,
            "phone": phone,
            "email": email
        }
        # Add the contact to the list of contacts
        self.contacts.append(contact)
        print(f"Contact {name} added successfully.")

    def list_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            for contact in self.contacts:
                # Print the details of each contact
                print(f"Name: {contact['name']}, Phone: {
                      contact['phone']}, Email: {contact['email']}")

    def save_contacts(self, filename):
        with open(filename, 'w') as file:
            # Write the contacts list to a JSON file
            json.dump(self.contacts, file)
        print(f"Contacts saved to {filename}.")

    def load_contacts(self, filename):
        try:
            with open(filename, 'r') as file:
                # Load the contacts from a JSON file
                self.contacts = json.load(file)
            print(f"Contacts loaded from {filename}.")
        except FileNotFoundError:
            print("File not found.")

    def menu(self):
        while True:
            print("\nContact Book Menu:")
            print("1. Add Contact")
            print("2. List Contacts")
            print("3. Save Contacts")
            print("4. Load Contacts")
            print("5. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                name = input("Enter name: ")
                phone = input("Enter phone: ")
                email = input("Enter email: ")
                self.add_contact(name, phone, email)
            elif choice == '2':
                self.list_contacts()
            elif choice == '3':
                filename = input("Enter filename to save: ")
                self.save_contacts(filename)
            elif choice == '4':
                filename = input("Enter filename to load: ")
                self.load_contacts(filename)
            elif choice == '5':
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    contact_book = ContactBook()
    contact_book.menu()
