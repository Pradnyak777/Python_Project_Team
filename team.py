# Data Storage
data_storage = {
    "A": ["sham","hyderabd"],  # Data filled by Field Executive A
    "B": ["kiran", "delhi"]   # Data filled by Field Executive B
}

# Access Control
roles = {
    "A": "Field Executive",
    "B": "Field Executive",
    "C": "Field Manager",
    "D": "Field Manager",
    "E": "Senior Manager"
}

# Functions for operations
def add_data(user):
    """Allow Field Executives to add data."""
    if roles[user] == "Field Executive":
        record = input(f"{user}, enter the data you want to add: ")
        data_storage[user].append(record)
        print(f"Data added successfully by {user}.\n")
    else:
        print("You do not have permission to add data.\n")

def view_data(user):
    """Allow users to view data based on their role."""
    if user == "A" or user == "B":
       
        # Field Executives can only see their own data
        print(f"Data for {user}: {data_storage[user]}\n")
    elif user == "C":
        
        # Manager C can see data from A and B
        print("Data accessible to Manager C:")
        print(f"Data from A: {data_storage['A']}")
        print(f"Data from B: {data_storage['B']}\n")
    elif user == "D":
        
        # Manager D cannot see data from A and B
        print("Manager D does not have access to Field Executive data.\n")
    elif user == "E":
        
        # Senior Manager can see all data
        print("Data accessible to Senior Manager E:")
        print(f"Data from A: {data_storage['A']}")
        print(f"Data from B: {data_storage['B']}\n")
    else:
        print("Invalid user.\n")

def update_data(user):
    """Allow Senior Manager to update any data."""
    if user == "E":
        exec = input("Enter the Field Executive (A or B) whose data you want to update: ")
        if exec in data_storage:
            print(f"Current data for {exec}: {data_storage[exec]}")
            idx = int(input(f"Enter the index of the record you want to update (0-based index): "))
            if 0 <= idx < len(data_storage[exec]):
                new_data = input("Enter the updated data: ")
                data_storage[exec][idx] = new_data
                print("Data updated successfully.\n")
            else:
                print("Invalid index.\n")
        else:
            print("Invalid Field Executive.\n")
    else:
        print("You do not have permission to update data.\n")

def delete_data(user):
    """Allow Senior Manager to delete any data."""
    if user == "E":
        exec = input("Enter the Field Executive (A or B) whose data you want to delete: ")
        if exec in data_storage:
            print(f"Current data for {exec}: {data_storage[exec]}")
            idx = int(input(f"Enter the index of the record you want to delete (0-based index): "))
            if 0 <= idx < len(data_storage[exec]):
                del data_storage[exec][idx]
                print("Data deleted successfully.\n")
            else:
                print("Invalid index.\n")
        else:
            print("Invalid Field Executive.\n")
    else:
        print("You do not have permission to delete data.\n")

# Menu for interaction
def menu():
    while True:
        print("\nRoles: A, B (Field Executives), C, D (Field Managers), E (Senior Manager)")
        user = input("Enter your role (A/B/C/D/E or 'exit' to quit): ").strip().upper()

        if user == "EXIT":
            print("Exiting program.")
            break

        if user in roles:
            print("\nAvailable actions:")
            print("1. Add Data (Only for Field Executives A and B)")
            print("2. View Data")
            print("3. Update Data (Only for Senior Manager E)")
            print("4. Delete Data (Only for Senior Manager E)")
            action = input("Choose an action (1/2/3/4): ").strip()

            if action == "1":
                add_data(user)
            elif action == "2":
                view_data(user)
            elif action == "3":
                update_data(user)
            elif action == "4":
                delete_data(user)
            else:
                print("Invalid action.\n")
        else:
            print("Invalid role.\n")

# Run the program
if __name__ == "__main__":
    menu()
