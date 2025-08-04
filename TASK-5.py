import json
import os

CONTACTS_FILE = "contacts.json"

def load_contacts():
    if not os.path.exists(CONTACTS_FILE):
        return []
    with open(CONTACTS_FILE, "r") as file:
        return json.load(file)

def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }

    contacts = load_contacts()
    contacts.append(contact)
    save_contacts(contacts)
    print("✅ Contact added successfully!")

def view_contacts():
    contacts = load_contacts()
    if not contacts:
        print("📭 No contacts found.")
        return
    print("\n--- Contact List ---")
    for idx, c in enumerate(contacts, start=1):
        print(f"{idx}. {c['name']} | {c['phone']}")

def search_contact():
    query = input("Search by name or phone: ").lower()
    contacts = load_contacts()
    found = [c for c in contacts if query in c['name'].lower() or query in c['phone']]
    if found:
        print("\n--- Search Results ---")
        for c in found:
            print(f"Name: {c['name']}\nPhone: {c['phone']}\nEmail: {c['email']}\nAddress: {c['address']}\n")
    else:
        print("❌ No matching contact found.")

def update_contact():
    name = input("Enter the name of the contact to update: ").lower()
    contacts = load_contacts()
    for c in contacts:
        if c['name'].lower() == name:
            print("Leave blank to keep current value.")
            c['phone'] = input(f"New phone ({c['phone']}): ") or c['phone']
            c['email'] = input(f"New email ({c['email']}): ") or c['email']
            c['address'] = input(f"New address ({c['address']}): ") or c['address']
            save_contacts(contacts)
            print("✅ Contact updated successfully!")
            return
    print("❌ Contact not found.")

def delete_contact():
    name = input("Enter the name of the contact to delete: ").lower()
    contacts = load_contacts()
    filtered = [c for c in contacts if c['name'].lower() != name]
    if len(filtered) == len(contacts):
        print("❌ Contact not found.")
    else:
        save_contacts(filtered)
        print("🗑 Contact deleted successfully!")

def main():
    while True:
        print("\n===== CONTACT BOOK MENU =====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("👋 Exiting Contact Book. Goodbye!")
            break
        else:
            print("❗ Invalid choice. Please try again.")

# Run the program
main()