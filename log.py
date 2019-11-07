#coding=utf-8
import time
import datetime

def save_action_to_log(taskitem,note):
    current_date = datetime.datetime.now()
    year = str(current_date.year)
    month = str(current_date.month)
    month = year + month
    log_file = open('task_log_'+month+'.txt','a+',encoding="utf-8")
    log_file.write(time.strftime('%Y.%m.%d %H:%M:%S', time.localtime(time.time()))+':   ')
    log_file.write('task_number:' + taskitem + note + '\n')
    log_file.close()

def save_something_to_log(something):
    current_date = datetime.datetime.now()
    year = str(current_date.year)
    month = str(current_date.month)
    month = year + month
    log_file = open('task_log_'+month+'.txt','a+',encoding="utf-8")
    log_file.write(time.strftime('%Y.%m.%d %H:%M:%S', time.localtime(time.time()))+':   ')
    log_file.write(something + '\n')
    log_file.close()

