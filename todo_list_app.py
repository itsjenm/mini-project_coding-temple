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
        tasks.append({"title": title, "status": "incomplete"})
        print(f"Tasks '{title}' added successfully!")
    else: 
        print("Task title cannot be empty.")