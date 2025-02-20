def add_employee():
    try:
        employee_id = get_user_input("Enter your employee id: ")
        name = input("Enter your name: ")
        position = input("Enter your position: ")
        salary = input("Enter your salary: ")
        record = f"{employee_id}, {name}, {position}, {salary}"
        with open("employees.txt", "a") as file:
            file.write(record)
    except Exception as e:
        print(f"An error occured {e}")

def get_user_input(prompt):
    try:
        return input(prompt)
    except (EOFError, OSError):
        print("Input operation is not allowed.")
        return "2"
def view_employees():
    try:
        with open("employees.txt", "r") as file:
            records = file.readlines()
            if records:
                print("\nEmployee records: ")
                for record in records:
                    print(record.strip())
                else:
                    print("\n No employee record found.")
                    
    except FileNotFoundError:
        print("\nThere is no such employee.")
    except Exception as e:
        print(f"An error occured {e}")
        
def search_employee():
    try:
        employee_id = get_user_input("Enter Employee ID to search: ")
        with open("employees.txt", "r") as file:
            records = file.readlines()
            found = False
            print("\nSearched by Employee ID: ")
            for record in records:
                if record.startswith(employee_id + ","):
                   print(record.strip()) 
                else:
                    print("\n No employee record found.")  
    except FileNotFoundError:
        print("\nThere is no such employee.")
    except Exception as e:
        print(f"An error occured {e}")    
        
        
def update_employee():
    try:
        employee_id = get_user_input("Enter Employee ID to update: ")
        updated_records = []
        found = False
        
        with open("employees.txt", "r") as file:
            records = file.readlines()
        
        for record in records:
            fields = record.strip().split(", ")
            if fields[0] == employee_id:
                print(f"Current Record: {record.strip()}")
                name = get_user_input("Enter new employee name: ") or fields[1]
                position = input("Enter new position: ") or fields[2] 
                salary = input("Enter new salary: ") or fields[3]
                updated_records.append(f"{name}, {position}, {salary}")
                found = True
            else:
                updated_records.append(record)
        if found:
            with open("employees.txt", "w") as file:
                file.writelines(updated_records)
            print("Updated")
        else:
            print("No such employee found.")
    except FileNotFoundError:
        print("\nThere is no such employee.")
    except Exception as e:
        print(f"An error occured {e}")  
        
def delete_employee():
    try:
        employee_id = get_user_input("Enter employee id to delete: ")
        updated_records = []
        found = False
        with open("employees.txt", "r") as file:
            records = file.readlines()
            
            for record in records:
                if not record.startswith(employee_id + ","):
                    updated_records.append(record)
                else:
                    found = True
            if found:
                with open("employees.txt", "w") as file:
                    file.writelines(updated_records)
                print("\n updated")
            else:
                print("No record")
            
    except FileNotFoundError:
        print("\nThere is no such employee.")
    except Exception as e:
        print(f"An error occured {e}")  
    
while True:
    print("Employee Records Manager")
    print("1. Add new employee record")
    print("2. View all employee records")
    print("3. Search for an employee by Employee ID")
    print("4. Update an employee's information")
    print("5. Delete an employee record")
    print("6. Exit")
    choice = get_user_input("Enter your choice: ")
    
    if choice == "1":
        add_employee()
    elif choice == "2":
        view_employees()
    elif choice == "3":
        search_employee()
    elif choice == "4":
        update_employee()
    elif choice == "5":
        delete_employee()
    elif choice == "6":
        print("Exiting program.")
        break
    else:
        print("Invalid choice.")