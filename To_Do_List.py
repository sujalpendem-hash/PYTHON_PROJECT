# todo_list.py

tasks = []

def show_tasks():
    if not tasks:
        print("No tasks yet!")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print("Task added!")

def remove_task():
    show_tasks()
    try:
        num = int(input("Enter task number to remove: "))
        removed = tasks.pop(num - 1)
        print(f"Removed task: {removed}")
    except (ValueError, IndexError):
        print("Invalid number!")

while True:
    print("\n--- TO-DO LIST ---")
    print("1. View tasks\n2. Add task\n3. Remove task\n4. Exit")

    choice = input("Choose an option: ")

    if choice == '1':
        show_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        remove_task()
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice!")
