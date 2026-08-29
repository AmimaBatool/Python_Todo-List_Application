#=====To-Do List Appplication=====

# List to store tasks
my_tasks = []   # List to store tasks


#-----FUNCTION DEFINATIONS-----

#Function to Add a New Task
def add_task(): 
    task = input("Enter a new task: ")
    my_tasks.append({"Task": task, "Status": "Pending.."})
    print("New Task Added Successfully!")
    print()


#Function to View all Tasks
def view_tasks():
    print("Your todo List: ")
    if len(my_tasks) == 0:
        print("No Pending Tasks! ")
    else: 
        for index, task in enumerate(my_tasks, 1):
            print(f"{index}: {task['Task']} - {task['Status']}")
    print()


#Function to Remove a Task
def remove_task():
    if len(my_tasks) == 0:
            print("List is Empty! ")
    else:
        search_index = int(input("Enter the Task Number you want to remove from the list:")) - 1
        if 0<= search_index < len(my_tasks):
            removed_task = my_tasks.pop(search_index)
            print(f"Task Removed:  {removed_task['Task']}")
        else:
            print("Invalid Task Number...")
    print()


#Function to Mark a Task as Completed
def mark_completed():
    if len(my_tasks) == 0:
            print("List is Empty! ")
    else:
        search_index = int(input("Enter the Task Number that you want to mark as completed:")) - 1
        if 0<= search_index < len(my_tasks):
            my_tasks[search_index]['Status'] = 'Completed'
            print(f"Task {my_tasks[search_index]['Task']} has been marked as completed..")
        else:
                print("Invalid Task Number...")
    print()


#Function to display a menu
def menu():
    while(True):
        print("----Main Menu----")
        print("1. Add a New Task")
        print("2. View all Tasks")
        print("3. Remove a task")
        print("4. Mark a task as Completed")
        print("5. Exit")
        print()

        choice = input("Enter your choice: ")
        print()
        if choice == "1":
            add_task()
        elif choice =="2":
            view_tasks()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            mark_completed()
        elif choice =="5":
            print("Exiting the application....")
            print()
            exit()
        else:
            print("Invalid choice! Try again!!")
            print()


menu()

