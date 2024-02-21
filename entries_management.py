
time_entries = {}
entry_id_counter = 1

def display_menu():
    print("\nTime Entry Management System")
    print("1. Create Time Entry")
    print("2. Update Time Entry")
    print("3. Delete Time Entry")
    print("4. View Time Entries")
    print("5. Exit")

def create_time_entry():
    global entry_id_counter
    employee = input("Enter Employee Name: ")
    project = input("Enter Project Name: ")
    while True:
            try:
                hours_worked = int(input("Enter Worked Hours: "))
                break 
            except ValueError:
                print("Error: Please enter a valid number for the hours worked.")
    
    time_entries[entry_id_counter] = {
        "Employee": employee,
        "Project": project,
        "Hours Worked": hours_worked
    }
    print(time_entries[entry_id_counter])
    print(f"Time entry created successfully with ID {entry_id_counter} :)")
    entry_id_counter += 1

def update_time_entry():
    entry_id = int(input("Enter Time Entry ID to Update: "))
    if entry_id in time_entries:
        employee = input("Enter new Employee Name: ")
        project = input("Enter new Project Name: ")
        while True:
            try:
                hours_worked = int(input("Enter Worked Hours: "))
                break 
            except ValueError:
                print("Error: Please enter a valid number for the hours worked.")
    
        time_entries[entry_id] = {
            "Employee": employee,
            "Project": project,
            "Hours Worked": hours_worked
        }
        print(f"Time entry {entry_id} updated successfully :)")

        # print(time_entries.keys())

    else:
        print("Time entry not found :(") 

def delete_time_entry():
    entry_id = int(input("Enter Time Entry ID to Delete: "))
    if entry_id in time_entries:
        del time_entries[entry_id]
        print(f"Time entry {entry_id} deleted successfully :)")
    else:
        print("Time entry not found :(")
        

def view_time_entries():
    if time_entries:
        print("\nTime Entries:")
        for entry_id, info in time_entries.items():
            print(f"ID: {entry_id}, Employee: {info['Employee']}, Project: {info['Project']}, Hours Worked: {info['Hours Worked']}")
    else:
        print("No time entries found :(")


def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            create_time_entry()
        elif choice == "2":
            update_time_entry()
        elif choice == "3":
            delete_time_entry()
        elif choice == "4":
            view_time_entries()
        elif choice == "5":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()

