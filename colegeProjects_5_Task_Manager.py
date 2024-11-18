'''create a list- store a list of tasks'''
tasks=[]


#add tasks


def add_task(title,description,priority='low',deadline=None):
    task={
        'title':title,
        'description':description,
        'priority':priority,
        'deadline':deadline,
        'status':'pending'
    }
    tasks.append(task)
def list_task():
    if not tasks:
        print("tasks not there")
    else:
        for i,task in enumerate(tasks,start=1):
            print(f'{task['title']}   -  {task['priority']}')
#Delete task
def delete_task(task_index):
    if task_index<0 or task_index >=len(tasks):
        print("invalid task number")
        return
    else:
        removed=tasks.pop(task_index) 
        print(f' task {removed["title"]} deleted')  
def toggle_status(task_index) :
    if task_index<0 or task_index >=len(tasks):
        print("invalid task number")
        return
    elif tashs[task_pindex]["status"]=='completed'
    else:
        tashs[task_pindex]["status"]=='pending'


# filter by priority
def filter_by_priority(prioority_level):
    filtered_task=[]
    # for task in tasks:
    #     if tasks['priority']==priority_level:
    #         fitered_task.append(task)
    # filtered_Task=[task for task in tasks if tasks['priority']==priority_level]
    fitered_tasks=list(filter(lambda task:task['priority']==priority_level,tasks))


#filter by date



          

#print tasks

add_task('given lab list','names of student','high','2024-11-13')
list_task()

# print(tasks)