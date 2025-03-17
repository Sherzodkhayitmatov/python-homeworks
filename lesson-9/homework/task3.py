import json
import os
import csv

class Task():
    def __init__(self, id, task, completed, priority):
        self.id = id
        self.task = task
        self.completed = completed
        self.priority = priority
        
    @staticmethod   
    def load(task_list):
        if not os.path.exists('tasks.json'):
            print("No such file")
            return
        
        with open('tasks.json', mode='r') as file:
            tasks = json.load(file)
            for task in tasks:
                task_obj = Task(task['id'], task['name'], task['description'], task['completed'])
                task_list.appemd(task_obj)
        print("Task done")
        Task.calculate_stats(task_list)
        
    @staticmethod
    def calculate_stats(task_list):
        total_tasks = len(task_list)
        completed_tasks = sum(1 for task in task_list if task.completed)
        pending_tasks = total_tasks - completed_tasks
        
        if total_tasks > 0:
            average_priority = sum(task.priority for task in task_list) / total_tasks
        else:
            average_priority = 0
            
        print(f"Total tasks: {total_tasks}")
        print(f"Completed tasks: {completed_tasks}")
        print(f"Pending tasks: {pending_tasks}")
        print(f"Average prioority: {average_priority}")
        
    @staticmethod
    def convert_to_csv(task_list, filename='tasks.csv'):
            with open(filename, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["ID", "Task", "Completed", "Priority"])
                
                
                for task in task_list:
                    writer.writerow([task.id, task.task, task.completed, task.priority])
                    
            print(f"Task saved: {filename}")
            
task_list = []
Task.load(task_list)
Task.convert_to_csv(task_list)