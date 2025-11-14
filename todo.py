
# To-Do List Application (Console-based)

# Load tasks from file
def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []


# Save tasks to file
def save_tasks(tasks):
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")


tasks = load_tasks()

while True:
    print("\n------ TO-DO LIST MENU ------")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    # View tasks
    if choice == "1":
        print("\nYour Tasks:")
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    # Add task
    elif choice == "2":
        new_task = input("Enter new task: ")
        tasks.append(new_task)
        save_tasks(tasks)
        print("Task added!")

    # Remove task
    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to remove!")
        else:
            task_no = int(input("Enter task number to remove: "))
            if 1 <= task_no <= len(tasks):
                removed_task = tasks.pop(task_no - 1)
                save_tasks(tasks)
                print(f"Removed: {removed_task}")
            else:
                print("Invalid task number!")

    # Exit
    elif choice == "4":
        print("Exiting... Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")

