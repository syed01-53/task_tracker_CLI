from pprint import pprint
import json
import os

# Filepath for the JSON file
FILEPATH = 'data.json'

# Read all data from the JSON file
def get_json_data():
    if os.path.exists(FILEPATH):
        try:
            with open(FILEPATH, 'r') as json_file:
                if os.stat(FILEPATH).st_size == 0:
                    return {}
                data = json.load(json_file)
            return data
        except json.JSONDecodeError:
            print("Error decoding JSON. Returning empty data.")
            return {}
    else:
        return {}

# Store data in the JSON file
def store_data_json(data):
    with open(FILEPATH, 'w') as store_file:
        json.dump(data, store_file, indent=4)

# Generate a new task ID
def generate_task_id(data):
    return str(len(data) + 1)

# Add a new task to the JSON file
def add_task(task):
    data = get_json_data()
    task_id = generate_task_id(data)
    current_data = {
        "id": task_id,
        "task": task
    }
    data[task_id] = current_data
    store_data_json(data)

# Update task based on ID
def update_task(id, new_task):
    data = get_json_data()
    if id in data:
        data[id]['task'] = new_task  # Update the task for the given ID
        store_data_json(data)
        print(f"Task with ID {id} has been updated.")
    else:
        print(f"Task with ID {id} not found.")

# Remove a task based on ID
def remove_task(id):
    data = get_json_data()
    if id in data:
        del data[id]  # Delete the task with the given ID
        store_data_json(data)
        print(f"Task with ID {id} has been removed.")
    else:
        print(f"Task with ID {id} not found.")

# Main function
def main():
    while True:
        print("\nSelect your task")
        print("add")
        print("update")
        print("remove")
        print("view (display tasks)")
        print("exit")

        choice = input("What's the action you want to perform? ")

        if choice == "add":
            task_desc = input("Enter task description: ")
            add_task(task_desc)
            print("Task added.")
        elif choice == "update":
            task_id = input("Enter task ID to update: ")
            new_task_desc = input("Enter new task description: ")
            update_task(task_id, new_task_desc)
        elif choice == "remove":
            task_id = input("Enter task ID to remove: ")
            remove_task(task_id)
        elif choice == "view":
            print("Current data in JSON file:")
            pprint(get_json_data())
        elif choice == "exit":
            print("Exiting the program.")
            break
        else:
            print("Invalid option selected")

        # Display the current contents of the JSON file
        print("\nCurrent data in JSON file:")
        pprint(get_json_data())

if __name__ == "__main__":
    main()
