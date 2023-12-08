import csv

def add_item(file_name):
    print("Add todo")
    # Ask the title of the todo
    todo_name = input("Enter a task: ")
    # Open file - list.csv 
    with open(file_name, "a") as f:
        writer = csv.writer(f)
    # Inserting values - title = user entered
                    # - completed = false
        writer.writerow([todo_name, "False"])

def remove_item(file_name):
    print("Remove todo")

def mark_item(file_name):
    print("Marked todo")

def view_todo(file_name):
    print("View todo")