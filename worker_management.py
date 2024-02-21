workers = {}
worker_id = None

def display_menu():
    print('\nWorkers Management System')
    print('1. Add worker')
    print('2. Update worker')
    print('3. Delete worker')
    print('4. View Workers')
    print('5. Exit')

def add_worker():
    fname = input("Enter First Name: ")
    lname = input("Enter Last Name: ")

    while True:
        try:
            hourly_rate = float(input("Enter Hourly Rate: "))
            break 
        except ValueError:
            print("Error: Please enter a valid number for the hourly rate.")
            
    global worker_id
    worker_id = fname.lower() + "_" + lname.lower()
    workers[worker_id] = {'First_Name': fname, 'Last_Name': lname, 'Hourly_Rate': hourly_rate}
    print(f"Worker {fname} {lname} added successfully.")

def update_worker():
    # worker_info = workers.values()
    if worker_id:
    # worker_id = input("Enter the worker's ID (First-Name_Last-Name) to update: ").lower()
    # if worker_id in workers:
        fname = input("Enter First Name:")
        lname = input("Enter Last Name:")
        
        while True:
            try:
                hourly_rate = float(input("Enter Hourly Rate: "))
                break 
            except ValueError:
                print("Error: Please enter a valid number for the hourly rate.")
    
        workers[worker_id] = {'First_Name':fname , 'Last_Name':lname, 'Hourly_Rate':hourly_rate}    
        print(f"Worker {fname} {lname} updated successfully.")
    else:
        print('Worker not found!!')




def delete_worker():
    worker_id = input("Enter the worker's ID (First-Name_Last-Name) to update: ").lower()
    if worker_id in workers:
        del workers[worker_id]
        print(f"Worker {worker_id} deleted successfully!!")
    else:
        print('Worker not found!!')


def view_workers():
    if workers:
        print('\nList of Workers:')
        for worker_id, info in workers.items():
            print(f"Worker_ID: {worker_id}, Name: {info['First_Name']} {info['Last_Name']}, Hourly Rate: ${info['Hourly_Rate']}")
    else:
        print('NO workers found!!')


def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            add_worker()
        elif choice == "2":
            update_worker()
        elif choice == "3":
            delete_worker()
        elif choice == "4":
            view_workers()
        elif choice == "5":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
