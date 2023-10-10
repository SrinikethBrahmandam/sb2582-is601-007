from datetime import datetime
import json
import os

tasks = []
# constant, don't edit, use .copy()
TASK_TEMPLATE = {
    "name":"",
    "due": None, # datetime
    "lastActivity": None, # datetime
    "description": "",
    "done": False # False if not done, datetime otherise
}

# don't edit, intentionaly left an unhandled exception possibility
def str_to_datetime(datetime_str):
    """ attempts to convert a string in one of two formats to a datetime
    Valid formats (visual representation): mm/dd/yy hh:mm:ss or yyyy-mm-dd hh:mm:ss """
    try:
        return datetime.strptime(datetime_str, '%m/%d/%y %H:%M:%S')
    except:
        return datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S')

def save():
    """ writes the tasks list to a json file to persist changes """
    f = open("tracker.json", "w")
    f.write(json.dumps(tasks, indent=4, default=str))
    f.close()

def load():
    """ loads the task list from a json file """
    if not os.path.isfile("tracker.json"):
        return
    f = open("tracker.json", "r")
    
    data = json.load(f)
    # Note about global keyword: https://stackoverflow.com/a/11867510
    global tasks
    tasks = data
    f.close()
    print(f"data {data}")    

def list_tasks(_tasks):
    """ List a summary view of all tasks """
    i = 0
    for t in _tasks:
        print(f"{i+1}) [{'x' if t['done'] else ' '}] Task: {t['name']} (Due: {t['due']})")
        i += 1
    if len(_tasks) == 0:
        print("No tasks to show")

# edits should happen below this line

def add_task(name: str, description: str, due: str):
    """ Copies the TASK_TEMPLATE and fills in the passed in data then adds the task to the tasks list """
    task = TASK_TEMPLATE.copy() # don't delete this; use this task reference for the below requirements
    # update lastActivity with the current datetime value
    task['lastActivity'] = datetime.now()
    # set the name, description, and due date (all must be provided)
    if name and description and due:
        try:
        # due date must match one of the formats mentioned in str_to_datetime()
            task['name'] = name
            task['description'] = description
            task['due'] = str_to_datetime(due)
            tasks.append(task)
            print("New task added successfully!")
        except ValueError: 
            print("Failed to add task. Name, description, and due date must be provided.")
    else:
        print("Failed to add task. Due date must be provided in one of the following formats: mm/dd/yy hh:mm:ss or yyyy-mm-dd hh:mm:ss")

    save()
    #sb2582-Sriniketh Brahmandam-10/9/23

def process_update(index):
    """ extracted the user input prompts to get task data then passes it to update_task() """
    if index < 0 or index >= len(tasks):
        print("Invalid task index.")
        return
    

    task = tasks[index]
    print(f"Updating task: {task['name']}")
    name = input(f"What's the name of this task? (TODO name) \n").strip()
    desc = input(f"What's a brief descriptions of this task? (TODO description) \n").strip()
    due = input(f"When is this task due (format: m/d/y H:M:S) (TODO due) \n").strip()
    update_task(index, name=name, description=desc, due=due)
    #sb2582-Sriniketh Brahmandam-10/9/23

def update_task(index: int, name: str, description:str, due: str):
    """ Updates the name, description , due date of a task found by index if an update to the property was provided """
    if index < 0 or index >= len(tasks):
        print("Invalid task index.")
        return
    
    task = tasks[index]
    original_task = task.copy()
    task['lastActivity'] = datetime.now()

    if name and name != original_task['name']:
        task['name'] = name
    if description and description != original_task['description']:
        task['description'] = description
    if due and str_to_datetime(due) != original_task['due']:
        task['due'] = str_to_datetime(due)

    # Check if any changes were made to the task properties
    if task != original_task:
        print("Task updated successfully!")
        save()
    else:
        print("No changes to save or no changes provided.")
    save()
    #sb2582-Sriniketh Brahmandam-10/9/23

def mark_done(index):
    """ Updates a single task, via index, to a done datetime"""
    
    if index < 0 or index >= len(tasks):
        print("Invalid task index.")
        return
    
    task = tasks[index]
    if task['done']:
        print("Task is already marked as done.")
    else:
        task['done'] = datetime.now()
        print("Task marked as done.")
        save()
    #sb2582-Sriniketh Brahmandam-10/9/23

def view_task(index):
    """ View more info about a specific task fetch by index """
    if index < 0 or index >= len(tasks):
        print("Invalid task index.")
        return
    
    task = tasks[index]
    completed_status = "Completed" if task['done'] else "Not Completed"
    
    print(f"Task: {task['name']}")
    print(f"Description: {task['description']}")
    print(f"Due Date: {task['due']}")
    print(f"Last Activity: {task['lastActivity']}")
    print(f"Status: {completed_status}")
    #sb2582-Sriniketh Brahmandam-10/9/23

def delete_task(index):
    """ deletes a task from the tasks list by index """
    if index < 0 or index >= len(tasks):
        print("Invalid task index. Deletion failed.")
        return
    
    deleted_task = tasks.pop(index)
    print(f"Task '{deleted_task['name']}' has been successfully deleted.")
    save()
    #sb2582-Sriniketh Brahmandam-10/9/23

def get_incomplete_tasks():
    """ prints a list of tasks that are not done """
    incomplete_tasks = [task for task in tasks if not task['done']]
    list_tasks(incomplete_tasks)
    #sb2582-Sriniketh Brahmandam-10/9/23
   
def get_overdue_tasks():
    """ prints a list of tasks that are over due completion (not done and expired) """
    current_time = datetime.now()
    overdue_tasks = [task for task in tasks if not task['done'] and task['due'] is not None and task['due'] < current_time]
    list_tasks(overdue_tasks)
    #sb2582-Sriniketh Brahmandam-10/9/23

def get_time_remaining(index):
    """ outputs the number of days, hours, minutes, seconds a task has before it's overdue otherwise shows similar info for how far past due it is """
    if index < 0 or index >= len(tasks):
        print("Invalid task index.")
        return
    
    task = tasks[index]

    if task['due'] is None:
        print("Task has no due date.")
        return
    
    current_time = datetime.now()
    time_difference = task['due'] - current_time

    if time_difference.days < 0:
        overdue_message = "overdue"
        time_difference = -time_difference
    else:
        overdue_message = "remaining"
    
    days = time_difference.days
    seconds = time_difference.seconds
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    print(f"{days} days, {hours} hours, {minutes} minutes, {seconds} seconds {overdue_message}")
    #sb2582-Sriniketh Brahmandam-10/9/23

# no changes needed below this line

command_list = ["add", "view", "update", "list", "incomplete", "overdue", "delete", "remaining", "help", "quit", "exit", "done"]
def print_options():
    """ prints a readable list of commands that can be typed when prompted """
    print("Choices")
    print("add - Creates a task")
    print("update - updates a specific task")
    print("view - see more info about a task by number")
    print("list - lists tasks")
    print("incomplete - lists incomplete tasks")
    print("overdue - lists overdue tasks")
    print("delete - deletes a task by number")
    print("remaining - gets the remaining time of a task by number")
    print("done - marks a task complete by number")
    print("quit or exit - terminates the program")
    print("help - shows this list again")

def run():
    """ runs the program until terminated or a quit/exit command is used """
    print("Welcome to Task Tracker!")
    load()
    print_options()
    while(True):
        opt = input("What would you like to do?\n").strip() # strip removes whitespace from beginning/end
        if opt not in command_list:
            print("That's not a valid option")
        elif opt == "add":
            name = input("What's the name of this task?\n").strip()
            desc = input("What's a brief descriptions of this task?\n").strip()
            due = input("When is this task due (visual format: mm/dd/yy hh:mm:ss)\n").strip()
            add_task(name, desc, due)
        elif opt == "view":
            num = int(input("Which task do you want to view? (hint: number from 'list') ").strip())
            index = num-1
            view_task(index)
        elif opt == "update":
            num = int(input("Which task do you want to update? (hint: number from 'list') ").strip())
            index = num-1
            process_update(index)
        elif opt == "done":
            num = int(input("Which task do you want to complete? (hint: number from 'list') ").strip())
            index = num-1
            mark_done(index)
        elif opt == "list":
            list_tasks(tasks)
        elif opt == "incomplete":
            get_incomplete_tasks()
        elif opt == "overdue":
            get_overdue_tasks()
        elif opt == "delete":
            num = int(input("Which task do you want to delete? (hint: number from 'list') ").strip())
            index = num-1
            delete_task(index)
        elif opt == "remaining":
            num = int(input("Which task do you like to get the duration for? (hint: number from 'list') ").strip())
            index = num-1
            get_time_remaining(index)
        elif opt in ["quit", "exit"]:
            print("Good bye.")
            quit()
        elif opt == "help":
            print_options()
        
if __name__ == "__main__":
    run()