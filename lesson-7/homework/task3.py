import os


class Task:
    def __init__(self, task_id, task_title, task_description, due_date, task_status):
        self.task_id = task_id
        self.task_title = task_title
        self.task_description = task_description
        self.due_date = due_date
        self.task_status = task_status
    
    def __str__(self):
        return f"{self.task_id}, {self.task_title}, {self.task_description}, {self.due_date}, {self.task_status}"

class ToDoApplication:
    FILE_NAME = "ToDoApplication.txt"
    
    @staticmethod
    def is_duplicate_id(task_id):
        if not os.path.exists(ToDoApplication.FILE_NAME):
            return False
        with open(ToDoApplication.FILE_NAME, "r") as file:
            for line in file:
                if line.startswith(task_id + ","):
                    return True
            return False
    
    
    
    @staticmethod
    def add_task():
        
        task_id = input("Enter Task ID: ").strip()
        
        if ToDoApplication.is_duplicate_id(task_id):
            print(f"There is a task with {task_id} ID")
            return
        
        task_title = input("Enter Title: ")
        task_description = input("Enter Description: ")
        due_date = input("Enter Due Date: ")
        task_status = input("Enter Task Status (Pending/In Progress/Completed): ")
        
        new_task = Task(task_id, task_title, task_description, due_date, task_status)
        
        with open(ToDoApplication.FILE_NAME, "a") as file:
            file.write(str(new_task) + "\n")
        print("New task added successfully.")
        
    @staticmethod   
    def view_task(sort_by=None):
        if not os.path.exists(ToDoApplication.FILE_NAME):
            print("No task found.")
            return
        
        with open(ToDoApplication.FILE_NAME, "r") as file:
            records = [line.strip() for line in file.readlines()]
            
        if not records:
            print("No task found.")
            return
        
        if sort_by:
            if sort_by == "task_title":
                records.sort(key=lambda x: x.split(", ")[1].lower())
            elif sort_by == "due_date":
                records.sort(key=lambda x: x.split(", ")[3])
            elif sort_by == "task_status":
                records.sort(key=lambda x: x.split(", ")[4].lower())               
                
                        
        print("\nTask Records:")
        for record in records:
            print(record)
            
    @staticmethod    
    def update_tasks():
        task_id = input("Enter Task ID to update: ").strip()
        if not os.path.exists(ToDoApplication.FILE_NAME):
            print("No tasks found.")
            return
        
        updated_records = []
        found = False
        
        with open(ToDoApplication.FILE_NAME, "r") as file:
            for line in file:
                if line.startswith(task_id + ","):
                    print("Updating Task:", line.strip())
                    task_title = input("Enter new title: ").strip()
                    task_description = input("Enter new Description: ").strip()
                    due_date = input("Enter new Due Date: ").strip()
                    task_status = input("Enter new Task Status (Pending/In Progress/Completed): ").strip()
                    
                    updated_records.append(f"{task_id}, {task_title}, {task_description}, {due_date}, {task_status}")
                    found = True
                else:
                    updated_records.append(line)
        if found:
            with open(ToDoApplication.FILE_NAME, "w") as file:
                file.writelines(updated_records)
            print("Task updated")
        else:
            print("Task not found.")   
        
    @staticmethod    
    def delete_task():
        task_id = input("Enter Task ID to delete").strip()
        if not os.path.exists(ToDoApplication.FILE_NAME):
            print("No tasks found.")
            return        
        
        updated_records = []
        found = False
        
        with open(ToDoApplication.FILE_NAME, "r") as file:
            for line in file:
                if not line.startswith(task_id + ","):
                    updated_records.append(line)
                else:
                    found = True
                    
        if found:
            with open(ToDoApplication.FILE_NAME, "w") as file:
                file.writelines(updated_records)
                print("Task deleted successfully.")
        else:
            print("Task not found")   
                             
    @staticmethod    
    def filter_task():
        status_filter = input("Enter status to filter (Pending/In Progress/Completed): ")
        if not os.path.exists(ToDoApplication.FILE_NAME):
            print("No tasks found.")
            return   
        
        with open(ToDoApplication.FILE_NAME, "r") as file:
            records = [line.strip() for line in file.readlines()]
            
        filtered_records = [record for record in records if record.split(", ")[4].lower()==status_filter]
        
        if filtered_records:
            print("\nFiltered tasks:")
            for record in filtered_records:
                print(record)
        else:
            print("No tasks found.")
                    

        
    @staticmethod
    def menu():
        while True:
            print("\n === Welcome to the To-Do Application! ===")
            print("1. Add a new task.")
            print("2. View all tasks.")
            print("3. Update a task.")
            print("4. Delete a task.")
            print("5. Filter tasks by status.")
            print("6. Exit")
            
            choice = input("Enter your choice: ").strip()
            
            if choice == "1":
                ToDoApplication.add_task()
            elif choice == "2":
                ToDoApplication.view_task()
            elif choice == "3":
                ToDoApplication.update_tasks()
            elif choice == "4":
                ToDoApplication.delete_task()
            elif choice == "5":
                ToDoApplication.filter_task()
            elif choice == "6":
                print("Exiting program!.")
                break
            else:
                print("Invalid choice. Try again.")


if __name__ == "__main__":
    ToDoApplication.menu()           
            