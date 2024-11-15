import sys, os, time, json
from json import JSONDecodeError

FILENAME = "tasks.json"
first_part = os.path.split(__file__)[0]
file_path = os.path.abspath(os.path.join(first_part, "tasks.json"))
usage = "Usage: python3 task-cli.py option *args"


if not os.path.exists(file_path):
    open(file_path, 'w')


# ----------------------------------------------------
# this section handles getting and storing tasks on 
# json file
def dump_file(info):
    """saves the todolist to the json file"""
    with open(file_path, 'w') as fileobj:
        json.dump(info, fileobj, indent=2)

def load_file():
    """gets the todolist from the json file"""
    with open(file_path, 'r') as fileobj:
        result = json.load(fileobj)
    return result
# ----------------------------------------------------


# checks if ths json file is empty when getting the tasklist data
try:
    loaded = load_file()
except JSONDecodeError as e:
    loaded = dict()


task_dict = dict(**loaded)

def assist():
    """
    exits the program with termination message that 
    provides assistance
    """
    exit(f"for help: python3 task-cli.py --help")

def getTime():
    """return the current time"""
    return time.ctime()

def add(arg: list=[]) -> None:
    """
    adds items to the tasklist and saves it to the json file
    """
    heading = ' '.join(arg) if arg else assist()

    if heading:
        updatedAt = None
        my_dict = {}

        my_dict[heading] = {
            "status": "todo",
            "createdAt": getTime(),
            "updatedAt": updatedAt,
        }
        
        task_dict.update(my_dict)
        dump_file(task_dict)


def update(arg: list):
    """
    provided an index, it updates in the the task dict
    at that index
    """
    if not len(arg) > 1: assist()

    global task_dict
    id, new_head = arg[:]
    id = int(id)
    tasks = [(num, task) for num, task in enumerate(task_dict.keys(), start=1)]
    new_dict = {}

    for (item_num, heading) in tasks:
        if id == item_num:
            for key, value in task_dict.items():
                if heading == key:
                    new_dict[new_head] = value
                    new_dict[new_head]['updatedAt'] = getTime()
                else:
                    new_dict[key] = value
    
    task_dict = new_dict
    dump_file(task_dict)

 
def delete(arg: list):
    """
    provided an index, it deletes a task in the task
    dict at that index
    """
    if not arg: assist()
    
    id = int(arg[0])
    tasks = [(num, task) for num, task in enumerate(task_dict.keys(), start=1)]
    
    for (item_num, heading) in tasks:
        if id == item_num:
            del task_dict[heading]
    
    dump_file(task_dict)
    print("Done")


def display(arg: list=[], arg_val=""):
    """
    dislays all the tasks with their related information
    on the terminal
    """
    status = arg[0] if arg else arg_val
    position = 1

    if not status:
        for key, value in task_dict.items():
            print(f"{position}. {key}:")
            
            for k, v in value.items():
                print(f"\t{k}: {v}")
            position += 1
            
            print("-"*45)
        return
    
    if status not in ['done', 'todo', 'in-progress']:
        print(f"{status!r} IS NOT A VALID 'arg'")
        assist()
    else:
        display_by_status(status, position=position)
        

def display_by_key(heading: str, position: int):
    """
    given a keyword it displays the information of all
    tasks that contain that keyword
    """
    for key, value in task_dict.items():
        if key == heading:
            print(f"{position}. {key}:")
            
            for k, v in value.items():
                print(f"\t{k}: {v}")
            position += 1

            print("-"*45)
    

def display_by_status(status: str, position):
    """
    given a keyword to identify the status of a task
    it displays the information of all tasks that contain
    that keyword
    """
    for key, value in task_dict.items():
        if value['status'] == status:
            display_by_key(key, position)
            

def mark_done(arg: list, status="done"):
    """
    Sets the status of a task to 'done'
    """
    if arg:
        id = int(arg[0])
        tasks = [(num, task) for num, task in enumerate(task_dict.keys(), start=1)]
        
        for (item_num, heading) in tasks:
            if id == item_num:
                for key, value in task_dict.items():
                    task_dict[heading]['status'] = status
                    task_dict[heading]['updatedAt'] = getTime()
        
        dump_file(task_dict)


def mark_in_progress(arg: list):
    """
    Sets the status of a task to 'in-progress'
    """
    mark_done(arg, status="in-progress")


def info():
    """
    Provides more information about how to use
    this program
    """
    usage = "Usage: python3 task-cli.py"
    information = {
        "add": f"add's an item to the list.\n{usage} add 'text you want to add'",
        "update": f"update an item that exist in the list.\n{usage} item_number 'text you want to add' ",
        "delete": f"remove an item from the list.\n{usage} item_number",
        "list": 
        f"""
            display all items in the list.
            {usage} list args
            Note: args is OPTIONAL.
            args should be blank if you want a list of all items.
            args include: done, in-progress
            {usage} list done | {usage} list in-progress
            """,
        "mark-done": f"Sets the status of an item.\n{usage} mark-done item_number",
        "mark-in-progress": f"Sets the status of an item.\n{usage} mark-in-progress item_number",
    }
    return information

def display_info():
    all_info = info()
    for key, value in all_info.items():
        print(f"{key} -> {value}", end="\n\n")


def main():
    prompts = {
        "add": add,
        "update": update,
        "delete": delete,
        "list": display,
        "mark-done": mark_done,
        "mark-in-progress": mark_in_progress,
    }

    usage = "Usage: python3 task-cli.py option *args"
    if len(sys.argv) <= 1:
        print(usage)
        exit("for help: python3 task-cli.py --help")

    option = sys.argv[1]
    
    if option == "--help":
        display_info()
    elif option not in prompts.keys():
        print(usage)
        print(f"{option!r} IS NOT A VALID OPTION")
        print(f"for help: python3 task-cli.py --help")
    else:
        prompts[option](sys.argv[2:])



if __name__ == "__main__":
    ERROR_FILE = "errorlog.txt"
    base = os.path.split(os.path.abspath(__file__))[0]
    error_path = os.path.join(base, ERROR_FILE)

    if not os.path.exists(error_path):
        open(error_path, 'w')

    try:
        main()
    except Exception as e:
        with open(error_path, 'a') as fileobj:
            print(e, file=fileobj)
        print("-"*45)
