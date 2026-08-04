task_list=[]
while True:
    task = {'name':'','time':'','done':False}       #字典格式

    input_name = input('请输入任务:')
    input_time = input('请输入提醒时间:')

    task['name'] = input_name
    task['time'] = input_time

    task_list.append(task)
    print(task)