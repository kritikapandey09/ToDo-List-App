print("===== TO-DO LIST =====")
print("1. View Tasks")
print("2. Add Task")
print("3. Remove Task")
print("4. Exit")

choice = input("Enter your choice: ")

# -------------------- ADD TASK --------------------
if choice == "2":

    task = input("Enter a task: ")

    file = open("tasks.txt", "a")
    file.write(task + "\n")
    file.close()

    print("Task Added Successfully!")

# -------------------- VIEW TASKS --------------------
elif choice == "1":

    file = open("tasks.txt", "r")
    tasks = file.readlines()
    file.close()

    print("\n===== YOUR TASKS =====\n")

    if len(tasks) == 0:
        print("No tasks found!")

    else:
        for i in range(len(tasks)):
            print(f"{i+1}. {tasks[i].strip()}")

# -------------------- REMOVE TASK --------------------
elif choice == "3":

    file = open("tasks.txt", "r")
    tasks = file.readlines()
    file.close()

    if len(tasks) == 0:
        print("No tasks to remove!")

    else:

        print("\n===== YOUR TASKS =====\n")

        for i in range(len(tasks)):
            print(f"{i+1}. {tasks[i].strip()}")

        try:

            task_number = int(input("\nEnter task number to delete: "))

            if 1 <= task_number <= len(tasks):

                tasks.pop(task_number - 1)

                file = open("tasks.txt", "w")
                file.writelines(tasks)
                file.close()

                print("Task Removed Successfully!")

            else:
                print("Invalid task number!")

        except ValueError:
            print("Please enter numbers only!")

# -------------------- EXIT --------------------
elif choice == "4":
    print("Goodbye!")

# -------------------- INVALID MENU --------------------
else:
    print("Invalid choice! Please select a number between 1 and 4.")