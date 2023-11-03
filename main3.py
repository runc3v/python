tasks = {}

def add_tasks(task):
    tasks[task] = 'Not finished'
    print('Task successfully add! ')

def del_tasks(task):
    del tasks[task]
    print('Task successfully deleted! ')

def done_tasks(task):
    tasks[task] = 'Finished! '
    print('Task is finished! ')

def show_tasks():
    for key, value in tasks.items():
        print(key, value)

print('Hi! You can choose the some action: ', '1. Add task', '2. Delete task', '3. Finished the task', '4. Show the list of task', sep='\n')
while True:
    comand = input('Enter the comand: ').lower()
    if comand in ['1', 'add task', 'i want to add task']:
        task = input("Enter task: ")
        add_tasks(task)

    if comand in ["2", "delet task", "i want to delete task"]:
        task = input("Enter the task which you want to delete: ")
        del_tasks(task)

    if comand in ["3", "task is finished", "choose the task"]:
        task = input("Enter the task which you are finished: ")
        done_tasks(task)

    if comand in ["4", "print the list"]:
        show_tasks()

