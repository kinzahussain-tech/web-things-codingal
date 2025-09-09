# importing the module
import sys

# function to collect initial contacts
def initial_slambook():
    rows, cols = int(input("Please enter number of yours: ")), 5
    slam_book = []
    
    for i in range(rows):
        print("\nEnter contact %d details in the following order (ONLY):" % (i+1))
        print("NOTE: * indicates mandatory fields")
        print("....................................................")
        temp = []
        for j in range(cols):
            if j == 0:   # Name
                temp.append(str(input("Enter name*: ")))
                if temp[j] == '' or temp[j] == ' ':
                    sys.exit("Name is a mandatory field. Process exiting due to blank field...")
            if j == 1:   # Number
                temp.append(int(input("Enter number*: ")))
            if j == 2:   # Something about friend
                temp.append(str(input("Enter something about your friend: ")))
                if temp[j] == '' or temp[j] == ' ':
                    temp[j] = None
            if j == 3:   # DOB
                temp.append(str(input("Enter date of birth(dd/mm/yy): ")))
                if temp[j] == '' or temp[j] == ' ':
                    temp[j] = None
            if j == 4:   # Category
                temp.append(str(input("Enter category(Family/Friends/Work/Others): ")))
                if temp[j] == '' or temp[j] == ' ':
                    temp[j] = None

        slam_book.append(temp)

    return slam_book


# Menu function
def menu(slam_book):
    while True:
        print("\n*********** SLAMBOOK MENU ***********")
        print("1. Show all contacts")
        print("2. Search contact by name")
        print("3. Add new contact")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == "1":
            print("\n--- All Contacts ---")
            for contact in slam_book:
                print(contact)
        
        elif choice == "2":
            search_name = input("Enter the name to search: ")
            found = False
            for contact in slam_book:
                if contact[0].lower() == search_name.lower():
                    print("Contact found:", contact)
                    found = True
            if not found:
                print("No contact found with that name.")
        
        elif choice == "3":
            print("\n--- Add New Contact ---")
            new_contact = []
            new_contact.append(input("Enter name*: "))
            new_contact.append(int(input("Enter number*: ")))
            new_contact.append(input("Enter something about your friend: ") or None)
            new_contact.append(input("Enter date of birth(dd/mm/yy): ") or None)
            new_contact.append(input("Enter category(Family/Friends/Work/Others): ") or None)
            slam_book.append(new_contact)
            print("Contact added successfully!")
        
        elif choice == "4":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")


# Main Program
slam_book = initial_slambook()
menu(slam_book)
