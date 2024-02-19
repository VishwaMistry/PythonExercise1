
projects = {}

def display_menu():
    print('\nProject Management System')
    print('1. Add project')
    print('2. Update project')
    print('3. Delete project')
    print('4. View projects')
    print('5. Exit')

def add_project():
    project_name = input("Enter Project Name: ")
    budget = float(input("Enter Project Budget: "))
    employees = input("Enter employee IDs (comma-separated): ").split(',')
    projects[project_name] = {'Budget': budget, 'Employees': employees}
    print(f"Project {project_name} added successfully.")

def update_project():
    project_name = input("Enter Project Name to update: ")
    if project_name in projects:
        budget = float(input("Enter new Project Budget: "))
        employees = input("Enter new employee IDs (comma-separated): ").split(',')
        projects[project_name] = {'Budget': budget, 'Employees': employees}
        print(f"Project {project_name} updated successfully.")
    else:
        print("Project not found!!")

def delete_project():
    project_name = input("Enter Project Name to delete: ")
    if project_name in projects:
        del projects[project_name]
        print(f"Project {project_name} deleted successfully!!")
    else:
        print("Project not found!!")

def view_projects():
    if projects:
        print("\nList of Projects:")
        for name, info in projects.items():
            print(f"Project Name: {name}, Budget: ${info['Budget']}, Employees: {', '.join(info['Employees'])}")
    else:
        print("No projects found!!")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            add_project()
        elif choice == "2":
            update_project()
        elif choice == "3":
            delete_project()
        elif choice == "4":
            view_projects()
        elif choice == "5":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()