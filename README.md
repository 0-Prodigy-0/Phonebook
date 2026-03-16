# Phonebook CLI

A simple command-line contact manager that stores your contacts locally in a JSON file.

---

## Features

- Add new contacts (name, phone, email)
- View all saved contacts
- Search contacts by name
- Delete a contact
- Update an existing contact's details
- Data persists in a local `phonebook.json` file

---

## Requirements

- Python 3.6+
- No external libraries required (uses built-in `json` and `os`)

---

## Usage

Run the script from your terminal:

```bash
python phonebook.py
```

You'll be presented with a menu:

```
CONTACT BOOK:
1. Add Contact
2. View Contacts
3. Search Contact
4. Delete Contact
5. Update Contact
6. Exit
```

Enter the number of the action you want to perform.

---

## How It Works

| Option | Description |
|--------|-------------|
| **Add Contact** | Prompts for name, phone, and email, then saves to the JSON file |
| **View Contacts** | Lists all saved contacts with their details |
| **Search Contact** | Finds contacts whose name contains your search query |
| **Delete Contact** | Shows all contacts and lets you pick one to remove |
| **Update Contact** | Lets you edit the name, phone, or email of an existing contact |
| **Exit** | Closes the program |

---

## Data Storage

Contacts are saved in a `phonebook.json` file in the **same directory as the script**. The file is created automatically on first run.

Example format:

```json
{
    "contacts": [
        {
            "name": "john doe",
            "phone": "555-1234",
            "email": "john@example.com"
        }
    ]
}
```

> All names and emails are stored in lowercase.

---

## Project Structure

```
phonebook.py      # Main script
phonebook.json    # Auto-generated contacts file
README.md         # This file
```
