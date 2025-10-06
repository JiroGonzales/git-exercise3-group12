# toDoApp.py

tasks = []


def add_task(task):
    """Add a new task."""
    tasks.append(task)
    print("\n✅ Task added successfully!\n")


def show_tasks():
    """Display all tasks."""
    if not tasks:
        print("\n📋 No tasks yet.\n")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
        print()


def remove_task(task_number):
    """Remove a task safely."""
    try:
        index = task_number - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            print(f"\n❌ Removed task: {removed}\n")
        else:
            print("\n⚠️ Invalid task number!\n")
    except ValueError:
        print("\n⚠️ Please enter a valid number!\n")


def main():
    """Main program loop."""
    while True:
        print("==== TO-DO LIST APP ====")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Remove Task")
        print("4. Exit")
        choice = input("Enter your choice (1–4): ").strip()

        if choice == "1":
            task = input("Enter task: ").strip()
            if task:
                add_task(task)
            else:
                print("\n⚠️ Task cannot be empty!\n")
        elif choice == "2":
            show_tasks()
        elif choice == "3":
            if not tasks:
                print("\n⚠️ No tasks to remove!\n")
            else:
                try:
                    n = int(input("Enter task number to remove: "))
                    remove_task(n)
                except ValueError:
                    print("\n⚠️ Invalid input. Please enter a number.\n")
        elif choice == "4":
            print("\n👋 Exiting... Goodbye!\n")
            break
        else:
            print("\n⚠️ Invalid choice! Please choose between 1–4.\n")


if __name__ == "__main__":
    main()
