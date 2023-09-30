import os

# Define the To-Do List file
TODO_FILE = "todo.txt"

# Function to display the To-Do List
def display_todo_list():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as file:
            tasks = file.readlines()
            if tasks:
                print("Your To-Do List:")
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task.strip()}")
            else:
                print("Your To-Do List is empty.")
    else:
        print("Your To-Do List is empty.")

# Function to add a task to the To-Do List
def add_task(task):
    with open(TODO_FILE, "a") as file:
        file.write(task + "\n")
    print(f"Task '{task}' added to the To-Do List.")

# Function to remove a task from the To-Do List
def remove_task(task_number):
    try:
        with open(TODO_FILE, "r") as file:
            tasks = file.readlines()
        
        if 1 <= task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)
            
            with open(TODO_FILE, "w") as file:
                file.writelines(tasks)
            
            print(f"Task '{removed_task.strip()}' removed from the To-Do List.")
        else:
            print("Invalid task number. Please try again.")
    except FileNotFoundError:
        print("Your To-Do List is empty.")

# Main loop
while True:
    print("\n--- To-Do List Application ---")
    print("1. Display To-Do List")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Quit")
    
    choice = input("Enter your choice (1/2/3/4): ")
    
    if choice == "1":
        display_todo_list()
    elif choice == "2":
        task = input("Enter the task: ")
        add_task(task)
    elif choice == "3":
        display_todo_list()
        task_number = input("Enter the task number to remove: ")
        try:
            task_number = int(task_number)
            remove_task(task_number)
        except ValueError:
            print("Invalid input. Please enter a valid task number.")
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")
