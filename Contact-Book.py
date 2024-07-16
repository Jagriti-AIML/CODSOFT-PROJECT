import json
import os

class ContactManager:
    def __init__(self, filename='contacts.json'):
        self.filename = filename
        self.contacts = self.load_contacts()

    def load_contacts(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                return json.load(file)
        return []

    def save_contacts(self):
        with open(self.filename, 'w') as file:
            json.dump(self.contacts, file)

    def add_contact(self, name, phone, email, address):
        self.contacts.append({'name': name, 'phone': phone, 'email': email, 'address': address})
        self.save_contacts()

    def view_contacts(self):
        for i, contact in enumerate(self.contacts):
            print(f"{i}. {contact['name']} - {contact['phone']}")

    def search_contact(self, search_term):
        results = [contact for contact in self.contacts if search_term.lower() in contact['name'].lower() or search_term in contact['phone']]
        for contact in results:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}")

    def update_contact(self, index, name, phone, email, address):
        if 0 <= index < len(self.contacts):
            self.contacts[index] = {'name': name, 'phone': phone, 'email': email, 'address': address}
            self.save_contacts()

    def delete_contact(self, index):
        if 0 <= index < len(self.contacts):
            del self.contacts[index]
            self.save_contacts()

def main():
    manager = ContactManager()
    while True:
        print("\n1. Add Contact\n2. View Contact List\n3. Search Contact\n4. Update Contact\n5. Delete Contact\n6. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            manager.add_contact(name, phone, email, address)
        elif choice == '2':
            manager.view_contacts()
        elif choice == '3':
            search_term = input("Enter name or phone to search: ")
            manager.search_contact(search_term)
        elif choice == '4':
            index = int(input("Enter contact index to update: "))
            name = input("Enter new name: ")
            phone = input("Enter new phone: ")
            email = input("Enter new email: ")
            address = input("Enter new address: ")
            manager.update_contact(index, name, phone, email, address)
        elif choice == '5':
            index = int(input("Enter contact index to delete: "))
            manager.delete_contact(index)
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
