#coding=utf-8
import sqlite3

def init_table():
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()
    try:
        create_tb_cmd = '''
        create table if not exists task_table(
        TASKID INT,
        PRI INT,
        CONTENT TEXT,
        START_TIME TEXT,
        END_TIME TEXT,
        DUR_TIME INT,
        STATUS INT);
        '''
        # 主要就是上面的语句
        c.execute(create_tb_cmd)
    except:
        print("Create table failed")
        return False
    conn.commit()
    conn.close()

def insert_table(tid,pri,content,startt,endt,t,status):
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()
    try:
        create_tb_cmd = '''
        create table if not exists task_table(
        TASKID INT,
        PRI INT,
        CONTENT TEXT,
        START_TIME TEXT,
        END_TIME TEXT,
        DUR_TIME INT,
        STATUS INT);
        '''
        # 主要就是上面的语句
        c.execute(create_tb_cmd)
    except:
        print("Create table failed")
        return False
    c.execute("insert into task_table (TASKID,PRI,CONTENT,START_TIME,END_TIME,DUR_TIME,STATUS) values(%d,%d,'%s','%s','%s',%d,%d)" % (tid,pri,content,startt,endt,t,status))
    conn.commit()
    conn.close()

def insert_item(tid,end_time,dur_time,status):
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()
    c.execute("update task_table set END_TIME=?,DUR_TIME=?,STATUS=? where TASKID=?;",(end_time,dur_time,status,tid))
    conn.commit()
    c.close()
    conn.close()

def show_table():
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()
    c.execute("select * from task_table")
    values = c.fetchall()
    print(values)
    c.close()
    conn.close()

def get_tasks_max_id():
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()
    count = c.execute("select count(*) from sqlite_master where type = 'table' and name = 'task_table'")
    count_val = count.fetchone()
    if count_val[0]:
        c.execute("select max(TASKID) from task_table")
        values = c.fetchone()
        if not values[0]:
            values = [0,]
    else:
        print('table not exists')
        values = [0,]
    c.close()
    conn.close()
    return values[0]

def get_all_available_tasks():
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()
    c.execute("select * from task_table where STATUS = 0")
    values = c.fetchall()
    c.close()
    conn.close()
    return values