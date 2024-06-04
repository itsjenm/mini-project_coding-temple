# A list of all the tasks in the application
tasks = []

def display_menu():
    """
    This function displays the application command line interface with the main menu options

    Returns (string): 
        Menu:
        1. Add a task
        2. View tasks
        3. Mark a task as complete
        4. Delete a task
        5. Quit
    
    """

    print("\nWelcome to the To-Do List App!")
    print("Menu:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Mark a task as complete")
    print("4. Delete a task")
    print("5. Quit")


def add_task():
    """
    This function adds a new task to the to-do list

    Returns (string):
        Task added successfully! 
    """

    title = input("Enter the task title: ").strip()
    if title:
        tasks.append({"title": title, "status": "Incomplete"})
        print(f"Tasks '{title}' added successfully!")
    else: 
        print("Task title cannot be empty.")


def view_task():
    """

    This function displays all tasks with their status

    Returns (String):
        Tasks and their status
    """
    if not tasks:
        print("No tasks in the list.")
    else:
        print("\nTasks:")
        for i, task in enumerate(tasks):
            print(f"{i + 1}. {task['title']} - {task['status']}")


def mark_task_complete():
    """
    This function marks a task as complete

    Returns (String): Task completed or error message

    """
    view_task()
    if tasks:
        try:
            task_number = int(input("Enter the task number to mark as complete: "))
            if 1 <= task_number <= len(tasks):
                tasks[task_number - 1]["status"] = "Complete"
                print(f"Task '{tasks[task_number - 1]['title']}' marked as complete.")
            else:
                print("Invalid task number")
        except ValueError:
            print("Please enter a valid number.")


def delete_task():
    """
    This function deletes a task from the to-do list

    Returns (String): task deleted or error message

    """
    view_task()
    if tasks:
        try:
            task_number = int(input("Enter the task number to delete: "))
            if 1 <= task_number <= len(tasks):
                removed_task = tasks.pop(task_number - 1)
                print(f"Tasks '{removed_task['title']}' deleted successful.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")


def main():
    """
    Main function of the program 

    """
    while True:
        display_menu()
        try: 
            choice = int(input("Choose an option (1-5): "))
            if choice == 1:
                add_task()
            elif choice == 2:
                view_task()
            elif choice == 3:
                mark_task_complete()
            elif choice == 4:
                delete_task()
            elif choice == 5:
                print("Thank you for using the To-Do List App. Goodbye!")
                break
            else:
                print("Invalid choice. Please choose a number between 1 and 5.")
        except ValueError:
            print("Please enter a valid number.")
        finally:
            print("\n")

if __name__ == "__main__":
    main()