def add_Task():
    task=input("Enter the task to be added - ")
    task_list.append(task)

def view_Task():
    print("The task are - ")
    print(task_list)

def remove_task():
    view_Task()
    rTask=int(input("Enter the task to be removed - "))-1
    task_list.pop(rTask)
    #if rTask in task_list:
     #   del task_list[rTask]
    print("The task has beeen removed")


print("Welcome to the To Do List")

task_list=[]
while True:
    print("1. Add a task")
    print("2. View the tasks")
    print("3. Delete a task")
    print("4. Exit")

    ch=int(input("Enter coice -"))

    if(ch==1):
            add_Task()
    elif(ch==2):
        view_Task()
    elif(ch==3):
        remove_task()
    elif(ch==4):
        print("Exit")
        exit