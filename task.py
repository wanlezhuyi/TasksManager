#coding=utf-8
import time
import datetime
from db import *
from log import *

class task(object):
    task_number = get_tasks_max_id()

    def __init__(self,content,pri,start_time,end_time,time,status):
        self.no = task.task_number
        self.content = content
        self.pri = pri
        self.start_time = start_time
        self.end_time = end_time
        self.time = time
        self.status = status
        save_action_to_log(str(self.no) +'; '+self.content,'--新建了此任务')

    def get_task_counts(self):
        return task.task_number

    def add_task_counts(self):
        task.task_number += 1

    def save(self):
        self.no = task.task_number
        insert_table(self.get_task_counts(),self.pri,self.content,self.start_time,self.end_time,self.time,self.status)



