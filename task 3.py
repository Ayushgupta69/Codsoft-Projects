# Simple To-Do List Application

todo_list = []

while True:
    print("\n--- To-Do List Menu ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Remove Task")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        task = input("Enter a new task: ")
        todo_list.append({"task": task, "done": False})
        print("Task added!")

    elif choice == '2':
        if not todo_list:
            print("No tasks in the list.")
        else:
            print("\nYour Tasks:")
            for i, item in enumerate(todo_list, 1):
                status = "Done" if item["done"] else "Not Done"
                print(f"{i}. {item['task']} [{status}]")

    elif choice == '3':
        task_num = int(input("Enter task number to mark as done: "))
        if 1 <= task_num <= len(todo_list):
            todo_list[task_num - 1]["done"] = True
            print("Task marked as done!")
        else:
            print("Invalid task number.")

    elif choice == '4':
        task_num = int(input("Enter task number to remove: "))
        if 1 <= task_num <= len(todo_list):
            removed = todo_list.pop(task_num - 1)
            print(f"Removed task: {removed['task']}")
        else:
            print("Invalid task number.")

    elif choice == '5':
        print("Exit...")
        break

    else:
        print("Please enter a valid choice (1-5).")
