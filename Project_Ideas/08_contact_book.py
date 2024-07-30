# Contact Book
# Design a command-line application to store and manage contacts. Users should
# be able to add, view, and delete contacts. This will help you practice working with
# data structures like lists or dictionaries.

import json

def load_contacts(filename):
    try:
        with open(filename, 'r') as file:
            contacts = json.load(file)
    except FileNotFoundError:
        contacts = []
    return contacts

def view_contacts(contacts):
    for i, contact in enumerate(contacts):
        print(f'{i+1}. {contact}')

# This function should be executed everytime add or delete was performed
def save_contacts(contacts, filename):
    with open(filename, 'w') as file:
        json.dump(contacts, file)

def add_contact(contacts):
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    mobile_number = input("Enter mobile number: ")
    email_address = input("Enter email address: ")
    contacts.append({
        "first_name": first_name,
        "last_name": last_name,
        "mobile_number": mobile_number,
        "email_address": email_address
    })
    print("Contact added successfully")

def delete_contact(contacts):
    view_contacts(contacts)
    index = int(input("Enter the contact number to delete: "))
    contacts.pop(index-1)

def display_menu():
    print("Contact Book Menu")
    print("1. View all contacts")
    print("2. Add new contact")
    print("3. Delete a contact")
    print("4. Exit")

def main():
    filename = "contacts.json"
    contacts = load_contacts(filename)

    while True:
        display_menu()
        choice = int(input("Select from the menu: "))
        if choice == 1:
            view_contacts(contacts)
        elif choice == 2:
            add_contact(contacts)
            save_contacts(contacts, filename)
        elif choice == 3:
            delete_contact(contacts)
            save_contacts(contacts, filename)
        else:
            break
if __name__ == "__main__":
    main()
