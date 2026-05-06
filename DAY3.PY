phonebook = {
    "Amit":"9876543210",
    "Riya":"91234567890"
}

# Add Contact
def add_contact():
    name=input("Enter name:").upper()
    if name  in phonebook:
        print("Contact already exists")
    else:
        number = input("Enter number:")
        phonebook[name] = number
        print("Contact added successfully")


# Search Contact
def search_contact():
    search = input("Enter name to search:").upper()
    found = False
    for name ,number in phonebook.items():
        if search in name.upper():
            print(f"{name}:{number}")
            found = True
        if not found:
            print("Contact not found")
    
# Delete Contact
def delete_contact():
    search = input("enter name to delete:").upper()
    found = False
    for name in list(phonebook.keys()):
        if search in name.upper():
            del phonebook[name]
            print(f"{name} deleted")
            found = True
    if not found:
        print("Contact not found")

#Display all contacts
def display_contact():
    if not phonebook:
        print("phonebook is empty")
    else:
        print("-----Phonebook-----")
        for name,number in phonebook.items():
            print(f"{name}:{number}")

# Menu of phonebook
while True:
    print("--phonebook menu--")
    print("1. add contact")
    print("2. search contact")
    print("3. delete contact")
    print("4. display contact")
    print("5. exit")
    choice = int(input("Enter choice number:"))
    if choice==1:
        add_contact()
    elif choice==2:
        search_contact()
    elif choice == 3:
        delete_contact()
    elif choice ==4:
        display_contact()
    elif choice==5:
        print("Exit")
        break
    else:
        print("Invalid choice,Try again")