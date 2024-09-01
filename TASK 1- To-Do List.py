#TASK 1
# To-Do List

def display_menu():
    print("\nTo-Do List Menu:")
    print("1. View To-Do List")
    print("2. Add a Task")
    print("3. Update a Task")
    print("4. Delete a Task")
    print("5. Exit")

def view_tasks(tasks):
    if not tasks:
        print("No tasks in the list.")
    else:
        print("\nYour To-Do List:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def add_task(tasks):
    task = input("Enter a new task: ")
    tasks.append(task)
    print("Task added successfully.")

def update_task(tasks):
    if not tasks:
        print("No tasks to update.")
        return
    view_tasks(tasks)
    task_num = int(input("Enter the task number to update: "))
    if 1 <= task_num <= len(tasks):
        new_task = input("Enter the updated task: ")
        tasks[task_num - 1] = new_task
        print("Task updated successfully.")
    else:
        print("Invalid task number.")

def delete_task(tasks):
    if not tasks:
        print("No tasks to delete.")
        return
    view_tasks(tasks)
    task_num = int(input("Enter the task number to delete: "))
    if 1 <= task_num <= len(tasks):
        removed_task = tasks.pop(task_num - 1)
        print(f"Task '{removed_task}' deleted successfully.")
    else:
        print("Invalid task number.")

def main():
    tasks = []
    
    while True:
        display_menu()
        choice = input("Choose an option: ")
        
        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            update_task(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            print("Exiting To-Do List. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
