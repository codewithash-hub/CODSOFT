import sys

# variable to make colors for the messages.
RED = "\033[31m"
GREEN = "\033[32m"
RESET = "\033[0m"

# Class implementation of the TODO List Application.
class TODO:
    def __init__(self):
        self.todos = []

    def appendTask(self):
        task = input("Enter a task: ")
        self.todos.append(task)
        
        print({sys.stdout.write(GREEN + f"Task '{task}' has been added to the list! " + RESET)})
    
    def popTask(self):
        pass
    
    def viewTask(self):
        pass
    
    def closeApp(self):
        print("___________BYE___________")
        print()
        exit()
        

if __name__ == '__main__':
    # Creating an object for a class TODO
    obj_ToDo = TODO()
    
    # creating a loop for the project
    print("Welcome to the To-Do List App!!!")
    
    while True:
        print()
        print("Select one option below.")
        print("________________________\n")
        
        print("1. Add new task.")
        print("2. List all tasks.")
        print("3. Delete a task.")
        print("4. Exit")
        
        print("________________________\n")

        choice = int(input("Enter your chioce (between 1-4): "))
        
        if choice == 1:
            obj_ToDo.appendTask()
        elif choice == 2:
            obj_ToDo.viewTask()
        elif choice == 3:
            obj_ToDo.popTask()
        elif choice == 4:
            obj_ToDo.closeApp()
        else:
            print()
            print(f"{sys.stdout.write(RED + "Error: Invalid Input! " + RESET)}")
            
            