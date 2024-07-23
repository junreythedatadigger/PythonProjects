# To-Do List
# Create a simple to-do list application where users can add, remove, and mark
# tasks as complete. This project will help you practice working with lists and user
# input.

import json


# Function to load tasks from a file
def load_tasks(filename):
    try:
        with open(filename, 'r') as file:
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = []
    return tasks


# Function to save tasks to a file
def save_tasks(tasks, filename):
    with open(filename, 'w') as file:
        json.dump(tasks, file)


# Function to display the menu
def display_menu():
    print("To-Do List Menu:")
    print("1. View tasks")
    print("2. Add task")
    print("3. Delete task")
    print("4. Exit")


# Function to view tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks in the to-do list.")
    else:
        for i, task in enumerate(tasks):
            print(f"{i + 1}. {task}")


# Function to add a task
def add_task(tasks):
    task = input("Enter the task: ")
    tasks.append(task)
    print("Task added.")


# Function to delete a task
def delete_task(tasks):
    view_tasks(tasks)
    task_number = int(input("Enter the task number to delete: "))
    if 0 < task_number <= len(tasks):
        tasks.pop(task_number - 1)
        print("Task deleted.")
    else:
        print("Invalid task number.")


def main():
    filename = "tasks.json"
    tasks = load_tasks(filename)

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
            save_tasks(tasks, filename)
        elif choice == '3':
            delete_task(tasks)
            save_tasks(tasks, filename)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
