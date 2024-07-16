import json
import os

class ToDoList:
    def __init__(self, filename='todo_list.json'):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                return json.load(file)
        return []

    def save_tasks(self):
        with open(self.filename, 'w') as file:
            json.dump(self.tasks, file)

    def add_task(self, task):
        self.tasks.append({'task': task, 'done': False})
        self.save_tasks()

    def update_task(self, index, new_task):
        if 0 <= index < len(self.tasks):
            self.tasks[index]['task'] = new_task
            self.save_tasks()

    def mark_done(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]['done'] = True
            self.save_tasks()

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
            self.save_tasks()

    def list_tasks(self):
        for i, task in enumerate(self.tasks):
            status = 'Done' if task['done'] else 'Not Done'
            print(f"{i}. {task['task']} - {status}")

def main():
    todo_list = ToDoList()
    while True:
        print("\n1. Add Task\n2. Update Task\n3. Mark Task as Done\n4. Delete Task\n5. List Tasks\n6. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == '2':
            index = int(input("Enter task index to update: "))
            new_task = input("Enter new task: ")
            todo_list.update_task(index, new_task)
        elif choice == '3':
            index = int(input("Enter task index to mark as done: "))
            todo_list.mark_done(index)
        elif choice == '4':
            index = int(input("Enter task index to delete: "))
            todo_list.delete_task(index)
        elif choice == '5':
            todo_list.list_tasks()
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
