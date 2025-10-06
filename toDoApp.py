"""
To-Do List Application
Enhanced version with logic fixes, input validation, and improved user interface.
"""
 
# Global list to store tasks
tasks = []
 
 
def add_task(task):
    """Add a new task to the list."""
    tasks.append(task)
    print("\nTask added successfully!\n")
 
 
def show_tasks():
    """Display all current tasks."""
    if not tasks:
        print("\nNo tasks yet. Start by adding one!\n")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
        print()
 
 
def remove_task(task_number):
    """Remove a task by its number."""
    try:
        index = task_number - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            print(f"\nRemoved task: {removed}\n")
        else:
            print("\nInvalid task number.\n")
    except ValueError:
        print("\nPlease enter a valid number.\n")
 
 
def main():
    """Main program loop for the To-Do List App."""
    while True:
        print("===== TO-DO LIST APP =====")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Remove Task")
        print("4. Exit")
 
        choice = input("Enter your choice (1-4): ").strip()
 
        if choice == "1":
            # Add Task
            task = input("Enter task: ").strip()
            if task:
                add_task(task)
            else:
                print("\nTask cannot be empty!\n")
 
        elif choice == "2":
            # Show Tasks
            show_tasks()
 
        elif choice == "3":
            # Remove Task with confirmation
            if not tasks:
                print("\nNo tasks to remove!\n")
            else:
                try:
                    n = int(input("Enter task number to remove: "))
                    confirm = input(f"Are you sure you want to remove task {n}? (y/n): ").strip().lower()
                    if confirm == "y":
                        remove_task(n)
                    else:
                        print("\nTask not removed.\n")
                except ValueError:
                    print("\nInvalid input. Please enter a number.\n")
 
        elif choice == "4":
            # Exit
            print("\nExiting the app. Goodbye!\n")
            break
 
        else:
            # Invalid menu choice
            print("\nInvalid choice! Please select between 1-4.\n")
 
 
if __name__ == "__main__":
    main()