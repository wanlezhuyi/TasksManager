#coding=utf-8
from tkinter import *
from tkinter import ttk
import datetime
import threading
import time
from task import *
from log import *
import os


current_tasks_num_to_do = 0

class TasksManager:

    msec = 1000
    
    def __init__(self,master):
        self.master = master
        self.task_dtime = 0
        self.running1 = False
        self.running2 = False
        self.running3 = False
        self.running4 = False
        self.running5 = False
        self.running6 = False
        self.dt_good_flag = True
        self.dt_bad_flag = False
        self.good_time = 0
        self.bad_time = 0
        self.initWidgets()

    def update_good_time(self):
        if self.dt_good_flag:
            self.good_time += 1
            self.dt_bad_flag = False
            self.good_time_t.set(self.seconds_to_strshow(self.good_time))
            self.good_timer = self.date_frame.after(self.msec,self.update_good_time)

    def update_bad_time(self):
        if self.dt_bad_flag:
            self.bad_time += 1
            self.dt_good_flag = False
            self.bad_time_t.set(self.seconds_to_strshow(self.bad_time))
            self.bad_timer = self.date_frame.after(self.msec,self.update_bad_time)

    def dstart(self):
        self.good_time = 0
        self.dt_good_flag = True
        self.update_good_time()
        save_something_to_log('工作开始了!')

    def app_start(self):
        self.bad_time = 0
        self.dt_bad_flag = True
        self.update_bad_time()
        save_something_to_log('今天开始了!')

    def initWidgets(self):
        global tasks
        self.date_frame = Frame(self.master)
        self.date_frame.pack(side=TOP)
        self.good_time_t = StringVar()
        self.bad_time_t = StringVar()
        label_good_time =  Label(self.date_frame,text='Work time: ',width=12,height=2)
        label_good_time.grid(row=0,column=0)
        self.entry_good_time = ttk.Entry(self.date_frame, textvariable=self.good_time_t, width=18, font=('StSong', 20, 'bold'),
                                     foreground='blue')
        self.entry_good_time.grid(row=0,column=1)
        Label(self.date_frame,text=time.strftime('%Y-%m-%d',time.localtime(time.time())),width=14,height=2,font=('StSong','20','bold')).grid(row=0,column=2)
        label_bad_time = Label(self.date_frame, text='Bad time: ', width=12, height=2)
        label_bad_time.grid(row=0,column=3)
        self.entry_bad_time = ttk.Entry(self.date_frame, textvariable=self.bad_time_t, width=18,font=('StSong', 20, 'bold'),
                                         foreground='red')
        self.entry_bad_time.grid(row=0,column=4)
        #ttk.Button(self.date_frame, text='Go', command=self.dstart).grid(row=0,column=5)


        task_frame = Frame(self.master)
        task_frame.pack(side=TOP,fill=BOTH,expand=YES)
        label_task1 = Label(task_frame, text='任务1:',width = 8,height=2)
        label_task2 = Label(task_frame, text='任务2:',width = 8,height=2)
        label_task3 = Label(task_frame, text='任务3:',width = 8,height=2)
        label_task4 = Label(task_frame, text='任务4:',width = 8,height=2)
        label_task5 = Label(task_frame, text='任务5:',width = 8,height=2)
        label_task6 = Label(task_frame, text='任务6:',width = 8,height=2)
        label_task1.grid(row=0, column=0)
        label_task2.grid(row=1, column=0)
        label_task3.grid(row=2, column=0)
        label_task4.grid(row=3, column=0)
        label_task5.grid(row=4, column=0)
        label_task6.grid(row=5, column=0)

        self.st1 = StringVar()
        self.t1 = StringVar()
        if current_tasks_num_to_do > 0:
            self.st1.set(tasks[0][2])
            self.t1.set(self.seconds_to_strshow(tasks[0][5]))
        self.entry_task1 = ttk.Entry(task_frame,textvariable=self.st1,width=30,font=('Helvetica',20,'bold'),foreground='green')
        self.entry_task1.grid(row=0,column=1)
        label_t1 = Label(task_frame, text='耗时:', width=8, height=2)
        label_t1.grid(row=0,column=2)
        self.entry_t1 = ttk.Entry(task_frame,textvariable=self.t1,width=20,font=('Helvetica',20,'bold'),foreground='blue')
        self.entry_t1.grid(row=0,column=3)

        self.st2 = StringVar()
        self.t2 = StringVar()
        if current_tasks_num_to_do > 1:
            self.st2.set(tasks[1][2])
            self.t2.set(self.seconds_to_strshow(tasks[1][5]))
        self.entry_task2 = ttk.Entry(task_frame,textvariable=self.st2,width=30,font=('Helvetica',20,'bold'),foreground='green')
        self.entry_task2.grid(row=1,column=1)
        label_t2 = Label(task_frame, text='耗时:', width=8, height=2)
        label_t2.grid(row=1,column=2)
        self.entry_t2 = ttk.Entry(task_frame,textvariable=self.t2,width=20,font=('Helvetica',20,'bold'),foreground='blue')
        self.entry_t2.grid(row=1,column=3)

        self.st3 = StringVar()
        self.t3 = StringVar()
        if current_tasks_num_to_do > 2:
            self.st3.set(tasks[2][2])
            self.t3.set(self.seconds_to_strshow(tasks[2][5]))
        self.entry_task3 = ttk.Entry(task_frame,textvariable=self.st3,width=30,font=('Helvetica',20,'bold'),foreground='green')
        self.entry_task3.grid(row=2,column=1)
        label_t3 = Label(task_frame, text='耗时:', width=8, height=2)
        label_t3.grid(row=2,column=2)
        self.entry_t3 = ttk.Entry(task_frame,textvariable=self.t3,width=20,font=('Helvetica',20,'bold'),foreground='blue')
        self.entry_t3.grid(row=2,column=3)

        self.st4 = StringVar()
        self.t4 = StringVar()
        if current_tasks_num_to_do > 3:
            self.st4.set(tasks[3][2])
            self.t4.set(self.seconds_to_strshow(tasks[3][5]))
        self.entry_task4 = ttk.Entry(task_frame,textvariable=self.st4,width=30,font=('Helvetica',20,'bold'),foreground='green')
        self.entry_task4.grid(row=3,column=1)
        label_t4 = Label(task_frame, text='耗时:', width=8, height=2)
        label_t4.grid(row=3,column=2)
        self.entry_t4 = ttk.Entry(task_frame,textvariable=self.t4,width=20,font=('Helvetica',20,'bold'),foreground='blue')
        self.entry_t4.grid(row=3,column=3)

        self.st5 = StringVar()
        self.t5 = StringVar()
        if current_tasks_num_to_do > 4:
            self.st5.set(tasks[4][2])
            self.t5.set(self.seconds_to_strshow(tasks[4][5]))
        self.entry_task5 = ttk.Entry(task_frame,textvariable=self.st5,width=30,font=('Helvetica',20,'bold'),foreground='green')
        self.entry_task5.grid(row=4,column=1)
        label_t5 = Label(task_frame, text='耗时:', width=8, height=2)
        label_t5.grid(row=4,column=2)
        self.entry_t5 = ttk.Entry(task_frame,textvariable=self.t5,width=20,font=('Helvetica',20,'bold'),foreground='blue')
        self.entry_t5.grid(row=4,column=3)

        self.st6 = StringVar()
        self.t6 = StringVar()
        if current_tasks_num_to_do > 5:
            self.st6.set(tasks[5][2])
            self.t6.set(self.seconds_to_strshow(tasks[5][5]))
        self.entry_task6 = ttk.Entry(task_frame,textvariable=self.st6,width=30,font=('Helvetica',20,'bold'),foreground='green')
        self.entry_task6.grid(row=5,column=1)
        label_t6 = Label(task_frame, text='耗时:', width=8, height=2)
        label_t6.grid(row=5,column=2)
        self.entry_t6 = ttk.Entry(task_frame,textvariable=self.t6,width=20,font=('Helvetica',20,'bold'),foreground='blue')
        self.entry_t6.grid(row=5,column=3)

        buttont11 = ttk.Button(task_frame,text='start',command=self.start1)
        buttont11.grid(row=0,column=4)
        buttont12 = ttk.Button(task_frame,text='stop', command=self.stop1)
        buttont12.grid(row=0, column=5)
        buttont13 = ttk.Button(task_frame,text='delete', command=self.delete1)
        buttont13.grid(row=0, column=6)

        buttont21 = ttk.Button(task_frame,text='start',command=self.start2)
        buttont21.grid(row=1,column=4)
        buttont22 = ttk.Button(task_frame,text='stop', command=self.stop2)
        buttont22.grid(row=1, column=5)
        buttont23 = ttk.Button(task_frame,text='delete', command=self.delete2)
        buttont23.grid(row=1, column=6)

        buttont31 = ttk.Button(task_frame,text='start',command=self.start3)
        buttont31.grid(row=2,column=4)
        buttont32 = ttk.Button(task_frame,text='stop', command=self.stop3)
        buttont32.grid(row=2, column=5)
        buttont33 = ttk.Button(task_frame,text='delete', command=self.delete3)
        buttont33.grid(row=2, column=6)

        buttont41 = ttk.Button(task_frame,text='start',command=self.start4)
        buttont41.grid(row=3,column=4)
        buttont42 = ttk.Button(task_frame,text='stop', command=self.stop4)
        buttont42.grid(row=3, column=5)
        buttont43 = ttk.Button(task_frame,text='delete', command=self.delete4)
        buttont43.grid(row=3, column=6)

        buttont51 = ttk.Button(task_frame,text='start',command=self.start5)
        buttont51.grid(row=4,column=4)
        buttont52 = ttk.Button(task_frame,text='stop', command=self.stop5)
        buttont52.grid(row=4, column=5)
        buttont53 = ttk.Button(task_frame,text='delete', command=self.delete5)
        buttont53.grid(row=4, column=6)

        buttont61 = ttk.Button(task_frame,text='start',command=self.start6)
        buttont61.grid(row=5,column=4)
        buttont62 = ttk.Button(task_frame,text='stop', command=self.stop6)
        buttont62.grid(row=5, column=5)
        buttont63 = ttk.Button(task_frame,text='delete', command=self.delete6)
        buttont63.grid(row=5, column=6)

        task_button_frame = Frame(self.master)
        task_button_frame.pack(side=BOTTOM)
        Label(task_button_frame, text='内容:', width=12, height=2).pack(side=LEFT)
        self.t = StringVar()
        self.entry = ttk.Entry(task_button_frame,textvariable=self.t,width=30,font=('Helvetica',20,'bold')).pack(side=LEFT)
        Label(task_button_frame, text='优先级:', width=8, height=2).pack(side=LEFT)
        self.pt = StringVar()
        self.pentry = ttk.Entry(task_button_frame,textvariable=self.pt,width=8,font=('Helvetica',20,'bold')).pack(side=LEFT)
        button_quit = ttk.Button(task_button_frame, text='Quit', command=self.quit).pack(side=RIGHT, padx=5)
        button_add = ttk.Button(task_button_frame,text='add a task',command=self.add).pack(side=RIGHT,padx=5)
        Label(task_button_frame, text='(0-3)', width=8, height=6).pack(side=LEFT)

    def refresh_window(self):
        global tasks
        if self.running1:
            self.stop1()
        if self.running2:
            self.stop2()
        if self.running3:
            self.stop3()
        if self.running4:
            self.stop4()
        if self.running5:
            self.stop5()
        if self.running6:
            self.stop6()
        tasks = get_all_available_tasks()
        current_tasks_num_to_do = len(tasks)
        tasks = adjust_tasks_by_pri(tasks)
        self.st1.set('')
        self.t1.set('')
        self.st2.set('')
        self.t2.set('')
        self.st3.set('')
        self.t3.set('')
        self.st4.set('')
        self.t4.set('')
        self.st5.set('')
        self.t5.set('')
        self.st6.set('')
        self.t6.set('')
        self.t.set('')
        self.pt.set('')
        if current_tasks_num_to_do > 0:
            self.st1.set(tasks[0][2])
            self.t1.set(self.seconds_to_strshow(tasks[0][5]))
        if current_tasks_num_to_do > 1:
            self.st2.set(tasks[1][2])
            self.t2.set(self.seconds_to_strshow(tasks[1][5]))
        if current_tasks_num_to_do > 2:
            self.st3.set(tasks[2][2])
            self.t3.set(self.seconds_to_strshow(tasks[2][5]))
        if current_tasks_num_to_do > 3:
            self.st4.set(tasks[3][2])
            self.t4.set(self.seconds_to_strshow(tasks[3][5]))
        if current_tasks_num_to_do > 4:
            self.st5.set(tasks[4][2])
            self.t5.set(self.seconds_to_strshow(tasks[4][5]))
        if current_tasks_num_to_do > 5:
            self.st6.set(tasks[5][2])
            self.t6.set(self.seconds_to_strshow(tasks[5][5]))


    def handle_good_bad_time(self,good):
        if good:
            if self.dt_bad_flag:
                self.dt_good_flag = True
                self.update_good_time()
                self.date_frame.after_cancel(self.bad_timer)
        else:
            if self.dt_good_flag:
                self.dt_bad_flag = True
                self.update_bad_time()
                self.date_frame.after_cancel(self.good_timer)


    def seconds_to_strshow(self,seconds):
        seconds = int(seconds)
        hour = int(seconds / 3600)
        minute = int(seconds % 3600 / 60)
        second = seconds % 3600 % 60
        ret_str = str(hour) + ' h ' + str(minute) + ' m ' + str(second) + 's '
        return ret_str

    def time_update1(self):
        global tasks
        tasks[0] = list(tasks[0])
        tasks[0][5] += 1
        self.t1.set(self.seconds_to_strshow(tasks[0][5]))
        self.timer1 = self.master.after(self.msec, self.time_update1)

    def start1(self):
        global tasks
        if not self.running1:
            self.running1 = True
            self.time_update1()
            self.handle_good_bad_time(True)
            save_action_to_log(str(tasks[0][0]) + '  ' + tasks[0][2], '--任务开始')

    def stop1(self):
        global tasks
        if self.running1:
            self.master.after_cancel(self.timer1)
            self.running1 = False
            tasks[0] = list(tasks[0])
            insert_item(tasks[0][0], '0',tasks[0][5] , 0)
            save_action_to_log(str(tasks[0][0]) + '; '+ tasks[0][2], '--任务停止')
            self.handle_good_bad_time(False)

    def delete1(self):
        global tasks
        if self.running1:
            self.stop1()
        tasks[0] = list(tasks[0])
        end_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        insert_item(tasks[0][0],end_time,tasks[0][5],1)
        save_action_to_log(str(tasks[0][0]) + '; '+ tasks[0][2], '--任务删除')
        self.refresh_window()


    def time_update2(self):
        global tasks
        tasks[1] = list(tasks[1])
        tasks[1][5] += 1
        self.t2.set(self.seconds_to_strshow(tasks[1][5]))
        self.timer2 = self.master.after(self.msec, self.time_update2)

    def start2(self):
        global tasks
        if not self.running2:
            self.running2 = True
            self.time_update2()
            self.handle_good_bad_time(True)
            save_action_to_log(str(tasks[1][0]) + '; ' + tasks[1][2], '--任务开始')

    def stop2(self):
        global tasks
        if self.running2:
            self.master.after_cancel(self.timer2)
            self.running2= False
            tasks[1] = list(tasks[1])
            insert_item(tasks[1][0], '0', tasks[1][5], 0)
            save_action_to_log(str(tasks[1][0]) + '; ' + tasks[1][2], '--任务停止')
            self.handle_good_bad_time(False)

    def delete2(self):
        global tasks
        if self.running2:
            self.stop2()
        tasks[1] = list(tasks[1])
        end_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        insert_item(tasks[1][0],end_time,tasks[1][5],1)
        save_action_to_log(str(tasks[1][0]) + '; ' + tasks[1][2], '--任务删除')
        self.refresh_window()

    def time_update3(self):
        global tasks
        tasks[2] = list(tasks[2])
        tasks[2][5] += 1
        self.t3.set(self.seconds_to_strshow(tasks[2][5]))
        self.timer3 = self.master.after(self.msec, self.time_update3)

    def start3(self):
        global tasks
        if not self.running3:
            self.running3 = True
            self.time_update3()
            self.handle_good_bad_time(True)
            save_action_to_log(str(tasks[2][0]) + '; ' + tasks[2][2], '--任务开始')

    def stop3(self):
        global tasks
        if self.running3:
            self.master.after_cancel(self.timer3)
            self.running3 = False
            tasks[2] = list(tasks[2])
            insert_item(tasks[2][0], '0', tasks[2][5], 0)
            save_action_to_log(str(tasks[2][0]) + '; ' + tasks[2][2], '--任务停止')
            self.handle_good_bad_time(False)

    def delete3(self):
        global tasks
        if self.running3:
            self.stop3()
        tasks[2] = list(tasks[1])
        end_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        insert_item(tasks[2][0],end_time,tasks[2][5],1)
        save_action_to_log(str(tasks[2][0]) + '; ' + tasks[2][2], '--任务删除')
        self.refresh_window()

    def time_update4(self):
        global tasks
        tasks[3] = list(tasks[3])
        tasks[3][5] += 1
        self.t4.set(self.seconds_to_strshow(tasks[3][5]))
        self.timer4 = self.master.after(self.msec, self.time_update4)

    def start4(self):
        global tasks
        if not self.running4:
            self.running4 = True
            self.time_update4()
            self.handle_good_bad_time(True)
            save_action_to_log(str(tasks[3][0]) + '; ' + tasks[3][2], '--任务开始')

    def stop4(self):
        global tasks
        if self.running4:
            self.master.after_cancel(self.timer4)
            self.running4 = False
            tasks[3] = list(tasks[3])
            insert_item(tasks[3][0], '0', tasks[3][5], 0)
            save_action_to_log(str(tasks[3][0]) + '; ' + tasks[3][2], '--任务停止')
            self.handle_good_bad_time(False)

    def delete4(self):
        global tasks
        print('delete4')
        if self.running4:
            self.stop4()
        tasks[3] = list(tasks[3])
        end_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        insert_item(tasks[3][0],end_time,tasks[3][5],1)
        save_action_to_log(str(tasks[3][0]) + '; ' + tasks[3][2], '--任务删除')
        self.refresh_window()

    def time_update5(self):
        global tasks
        tasks[4] = list(tasks[4])
        tasks[4][5] += 1
        self.t5.set(self.seconds_to_strshow(tasks[4][5]))
        self.timer5 = self.master.after(self.msec, self.time_update5)

    def start5(self):
        global tasks
        if not self.running5:
            self.running5 = True
            self.time_update5()
            self.handle_good_bad_time(True)
            save_action_to_log(str(tasks[4][0]) + '; ' + tasks[4][2], '--任务开始')

    def stop5(self):
        global tasks
        if self.running5:
            self.master.after_cancel(self.timer5)
            self.running5 = False
            tasks[4] = list(tasks[4])
            insert_item(tasks[4][0], '0', tasks[4][5], 0)
            save_action_to_log(str(tasks[4][0]) + '; ' + tasks[4][2], '--任务停止')
            self.handle_good_bad_time(False)

    def delete5(self):
        global tasks
        if self.running5:
            self.stop5()
        tasks[4] = list(tasks[4])
        end_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        insert_item(tasks[4][0], end_time, tasks[4][5], 1)
        save_action_to_log(str(tasks[4][0]) + '; ' + tasks[4][2], '--任务删除')
        self.refresh_window()

    def time_update6(self):
        global tasks
        tasks[5] = list(tasks[5])
        tasks[5][5] += 1
        self.t6.set(self.seconds_to_strshow(tasks[5][5]))
        self.timer6 = self.master.after(self.msec, self.time_update6)

    def start6(self):
        global tasks
        if not self.running6:
            self.running6 = True
            self.time_update6()
            self.handle_good_bad_time(True)
            save_action_to_log(str(tasks[5][0]) + '; ' + tasks[5][2], '--任务开始')

    def stop6(self):
        global tasks
        if self.running6:
            self.master.after_cancel(self.timer6)
            self.running6 = False
            tasks[5] = list(tasks[5])
            insert_item(tasks[5][0], '0', tasks[5][5], 0)
            save_action_to_log(str(tasks[5][0]) + '; ' + tasks[5][2], '--任务停止')
            self.handle_good_bad_time(False)

    def delete6(self):
        global tasks
        if self.running6:
            self.stop6()
        tasks[5] = list(tasks[5])
        end_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        insert_item(tasks[5][0], end_time, tasks[5][5], 1)
        save_action_to_log(str(tasks[5][0]) + '; ' + tasks[5][2], '--任务删除')
        self.refresh_window()


    def add(self):
        global tasks
        start_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        t = task(self.t.get(),int(self.pt.get()), start_time, 0, 0,0)
        t.add_task_counts()
        t.save()
        self.refresh_window()

    def quit(self):
        self.stop1()
        self.stop2()
        self.stop3()
        self.stop4()
        self.stop5()
        self.stop6()
        time.sleep(0.3)
        save_something_to_log('今天有效工作了：' + self.seconds_to_strshow(self.good_time))
        save_something_to_log('今天有 ' + self.seconds_to_strshow(self.bad_time) + '不知道干啥了')
        save_something_to_log('今天结束了')
        os._exit(0)

    def quit_app_automatically(self):
        while True:
            time_now = int(time.localtime().tm_hour)
            if time_now > 21:
                save_something_to_log('忘记关app了!')
                break
            time.sleep()
        self.stop1()
        self.stop2()
        self.stop3()
        self.stop4()
        self.stop5()
        self.stop6()
        time.sleep(1)
        os._exit(0)

def adjust_tasks_by_pri(tasks):
    i = 0
    while i <= len(tasks)-1:
        j = i + 1
        while j <= len(tasks)-1:
            if tasks[i][1] > tasks[j][1]:
                temp = tasks[j]
                tasks[j] = tasks[i]
                tasks[i] = temp
            j += 1
        i += 1
    return tasks




if __name__ == '__main__':
    global tasks
    init_table()
    tasks = get_all_available_tasks()
    current_tasks_num_to_do = len(tasks)
    tasks = adjust_tasks_by_pri(tasks)
    root = Tk()
    root.geometry('1100x300')
    root.title('任务管理')
    tm = TasksManager(root)
    t = threading.Thread(target=tm.quit_app_automatically)
    t.start()
    tm.app_start()
    root.mainloop()






