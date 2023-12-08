from todo_functions import add_item, remove_item, mark_item, view_todo

file_name = "./Saturday/Revision/list.csv"

try:
    #  open the file in read mode
    todo_file = open(file_name, "r")
    todo_file.close()
    print("In try clock")
    # if it throws error, means the file doesn't exist
    # if no error, it means the file exists
except FileNotFoungdError:
    # now we know the file doesn't exist
    # create the file
    todo_file = open(file_name, "w")
    # we can also insert the first line into the file
    todo_file.write("title,completed\n")
    todo_file.close()
    print("In except block")

print("Welcome to your TODO list")

def create_menu():
    print("1. Enter 1 to add item to your list")
    print("2. Enter 2 to remove item from your list")
    print("3. Enter 3 to mark an item as completed")
    print("4. Enter 4 to view your todo list")
    print("5. Enter 5 to exit")
    choice = input("Enter your selection: ")
    return choice

users_choice = ""

while users_choice != "5":
    users_choice = create_menu()
    if (users_choice == "1"):
        add_item(file_name)
    elif (users_choice == "2"):
        remove_item()
    elif (users_choice == "3"):
        mark_item()
    elif (users_choice == "4"):
        view_todo()
    elif (users_choice == "5"):
        continue
    else:
        print("Invalid Input")

print("Thank you for using todo list")