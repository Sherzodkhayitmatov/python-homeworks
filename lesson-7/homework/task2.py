import os

class Employee:
    def __init__(self, employee_id, name, position, salary):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
        return f"{self.employee_id}, {self.name}, {self.position}, {self.salary}"


class EmployeeManager:
    FILE_NAME = "employees.txt"
    
    @staticmethod
    def add_employee():
        employee_id = input("Enter Employee ID: ").strip()
        if EmployeeManager.is_duplicate_id(employee_id):
            print("Error: Employee ID already exists!")
            return
        
        name = input("Enter Name: ").strip()
        position = input("Enter Position: ").strip()
        salary = input("Enter Salary: ").strip()
        
        new_employee = Employee(employee_id, name, position, salary)
        
        with open(EmployeeManager.FILE_NAME, "a") as file:
            file.write(str(new_employee) + "\n")
        print("Employee added successfully!")
    
    @staticmethod
    def view_all_employees(sort_by=None):
        if not os.path.exists(EmployeeManager.FILE_NAME):
            print("No employee records found.")
            return
        
        with open(EmployeeManager.FILE_NAME, "r") as file:
            records = [line.strip() for line in file.readlines()]
        
        if not records:
            print("No employee records found.")
            return
        
        if sort_by:
            if sort_by == "name":
                records.sort(key=lambda x: x.split(", ")[1])
            elif sort_by == "salary":
                records.sort(key=lambda x: float(x.split(", ")[3]))
        
        print("\nEmployee Records:")
        for record in records:
            print(record)
    
    @staticmethod
    def search_employee():
        employee_id = input("Enter Employee ID to search: ").strip()
        with open(EmployeeManager.FILE_NAME, "r") as file:
            for line in file:
                if line.startswith(employee_id + ","):
                    print("Employee Found:")
                    print(line.strip())
                    return
        print("No employee found with that ID.")
    
    @staticmethod
    def update_employee():
        employee_id = input("Enter Employee ID to update: ").strip()
        updated_records = []
        found = False
        
        with open(EmployeeManager.FILE_NAME, "r") as file:
            for line in file:
                fields = line.strip().split(", ")
                if fields[0] == employee_id:
                    print(f"Current Record: {line.strip()}")
                    name = input("Enter new name (press Enter to keep current): ").strip() or fields[1]
                    position = input("Enter new position (press Enter to keep current): ").strip() or fields[2]
                    salary = input("Enter new salary (press Enter to keep current): ").strip() or fields[3]
                    updated_records.append(f"{employee_id}, {name}, {position}, {salary}\n")
                    found = True
                else:
                    updated_records.append(line)
        
        if found:
            with open(EmployeeManager.FILE_NAME, "w") as file:
                file.writelines(updated_records)
            print("Employee record updated successfully!")
        else:
            print("No such employee found.")
    
    @staticmethod
    def delete_employee():
        employee_id = input("Enter Employee ID to delete: ").strip()
        updated_records = []
        found = False
        
        with open(EmployeeManager.FILE_NAME, "r") as file:
            for line in file:
                if not line.startswith(employee_id + ","):
                    updated_records.append(line)
                else:
                    found = True
        
        if found:
            with open(EmployeeManager.FILE_NAME, "w") as file:
                file.writelines(updated_records)
            print("Employee record deleted successfully!")
        else:
            print("No such employee found.")
    
    @staticmethod
    def is_duplicate_id(employee_id):
        if not os.path.exists(EmployeeManager.FILE_NAME):
            return False
        with open(EmployeeManager.FILE_NAME, "r") as file:
            for line in file:
                if line.startswith(employee_id + ","):
                    return True
        return False
    
    @staticmethod
    def menu():
        while True:
            print("\n=== Employee Records Manager ===")
            print("1. Add new employee record")
            print("2. View all employee records")
            print("3. Search for an employee by Employee ID")
            print("4. Update an employee's information")
            print("5. Delete an employee record")
            print("6. Exit")
            choice = input("Enter your choice: ").strip()
            
            if choice == "1":
                EmployeeManager.add_employee()
            elif choice == "2":
                sort_by = input("Sort by (name/salary/none): ").strip().lower()
                sort_by = sort_by if sort_by in ["name", "salary"] else None
                EmployeeManager.view_all_employees(sort_by)
            elif choice == "3":
                EmployeeManager.search_employee()
            elif choice == "4":
                EmployeeManager.update_employee()
            elif choice == "5":
                EmployeeManager.delete_employee()
            elif choice == "6":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    EmployeeManager.menu()
