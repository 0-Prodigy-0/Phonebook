import json

filename = "phonebook.json"

try:    
    with open(filename, "r") as f:
        data = json.load(f)
except FileNotFoundError:
    with open(filename, "w") as f:
        json.dump({"contacts":[]}, f)

def add_Contact():
    person = {}
    person["name"] = input("Contact name: ").lower()
    person["phone"] = input("Contact phone number: ").lower()
    person["email"] = input("Contact email: ").lower()
    try:
        with open(filename, "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {"contacts": []}
    except json.JSONDecodeError:
        print("Contacts file is corrupted!")
        return
    data["contacts"].append(person)
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)
    print(f"{person['name']} added to your contacts")

def view_contacts():
    try:
        with open(filename, "r") as f:
            data = json.load(f)
        contacts = data["contacts"]
        if len(contacts) == 0:
            print("No contacts found!")
            return
        print(f"\n📒 You have {len(contacts)} contact(s):\n")
        for i, contact in enumerate(contacts, 1):
            print(f"{i}. Name:  {contact['name']}")
            print(f"   Phone: {contact['phone']}")
            print(f"   Email: {contact['email']}")
            print("-" * 30)
    except FileNotFoundError:
        print("No contacts file found! Add a contact first.")
    except json.JSONDecodeError:
        print("Contacts file is corrupted!")

def search_Contact():
    try:
        with open(filename, "r") as f:
            data = json.load(f)
        contact_Name = input("Enter contact name: ").lower()
        found = False
        for i in data['contacts']:
            if contact_Name in i['name']:
                print(f"{i['name']}: {i['phone']}, {i['email']}")
                found = True
        if not found:
            print("No contact found")
    except json.JSONDecodeError:
        print("Contact file is corrupted!")
    except FileNotFoundError:
        print("No contacts file found! Create a contacts file first!")

def delete_contact():
    try:
        with open(filename, "r") as f:
            data = json.load(f)
        contacts = data["contacts"]
        if len(contacts) == 0:
            print("No contacts to delete!")
            return
        print("\n📒 Your contacts:\n")
        for i, contact in enumerate(contacts, 1):
            print(f"{i}. {contact['name']} - {contact['phone']}")
        choice = int(input("\nEnter the number of the contact to delete: "))
        if choice < 1 or choice > len(contacts):
            print("Invalid number!")
            return
        removed = contacts.pop(choice - 1)
        data["contacts"] = contacts
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)
        print(f"\n🗑️ '{removed['name']}' has been deleted!")
    except FileNotFoundError:
        print("No contacts file found! Add a contact first.")
    except json.JSONDecodeError:
        print("Contacts file is corrupted!")
    except ValueError:
        print("Please enter a valid number!")

def update_Contact():
    def save():
        data['contacts'] = contacts
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)
    try:
        with open(filename, "r") as f:
            data = json.load(f)
        contacts = data["contacts"]
        print("\n📒 Your contacts:\n")
        for i, contact in enumerate(contacts, 1):
            print(f"{i}. {contact['name']} - {contact['phone']}")
        try:
            choice = int(input("Enter the number of the contact to update: "))
        except ValueError:
            print("Invalid entry")
            return
        if choice < 1 or choice > len(contacts):
            print("Invalid number")
            return
        value = input("What do you want to change? (name/phone/email): ")
        if value.lower() == "name":
            contacts[choice-1]['name'] = input("Enter the new name: ")
            save()
        elif value.lower() == "phone":
            contacts[choice-1]['phone'] = input("Enter the new phone: ")
            save()
        elif value.lower() == "email":
            contacts[choice-1]['email'] = input("Enter the new email: ")
            save()
        else:
            print("Invalid field")
    except FileNotFoundError:
        print("Contacts file does not exist")
    except json.JSONDecodeError:
        print("File is corrupted")

def main():
    while True:
        print("\nCONTACT BOOK:\n1. Add Contact\n2. View Contacts\n3. Search Contact\n4. Delete Contact\n5. Update Contact\n6. Exit")
        try:
            user = int(input("Enter your choice (1-6): "))
        except ValueError:
            print("Invalid input")
            continue
        if user == 1:
            add_Contact()
        elif user == 2:
            view_contacts()
        elif user == 3:
            search_Contact()
        elif user == 4:
            delete_contact()
        elif user == 5:
            update_Contact()
        elif user == 6:
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
