import tkinter as tk
import time
import random
import threading as td

# -*- coding: UTF-8 -*-

class gunlun:

        employee_name_list = []
        employee_winers_num = 1 # the NUB of each level winer


        def __init__(self):
                self.run_f = 0

                # create windown
                self.window = tk.Tk()
                self.window.title('Lottery')
                self.window.geometry('1024x800')

                self.backpng = tk.Canvas(self.window, height=800, width=1024)#创建画布
                self.photo = tk.PhotoImage(file="BACK2GIF.gif")
                self.image = self.backpng.create_image(0,0, anchor='nw', image=self.photo)#将图片置于画布上
                self.backpng.pack(side='top')#放置画布（为上端）


                
                # self.backpng = tk.Label(self.window,text='kan!!!!!!!!!!!', justify=tk.LEFT,image=photo,compound = tk.CENTER)#背景图片的代码
                # self.backpng.pack()
                 

                # self.window.configure(bg='#778899')
    
                self.window.resizable(width=False, height=False)

                # how many winer get
                self.winer_num_lable = tk.Label(self.window, text='本轮中奖人数:', font=('宋体', 14), width=12, height=1)
                self.winer_num_lable.place(x=710, y=435)

                self.winer_num = tk.StringVar()
                self.winer_num.set('1')
                self.entry_winer_num = tk.Entry(self.window, width=5, font=('Arial', 14), textvariable=self.winer_num,)
                self.entry_winer_num.place(x=850, y=435)

                # show final winer
                self.winer_name_lable = tk.Label(self.window, text='恭喜获奖者:', font=('宋体', 20), width=15, height=1)
                self.winer_name_lable.place(x=10, y=310)

                self.winer_show = tk.StringVar()#获奖名单展示
                self.winer_show.set('')
                self.entry_winer_show = tk.Label(self.window, font=('宋体', 20),fg='Crimson',bg='white', textvariable=self.winer_show, width=30,wraplength =120,height =15,justify = 'left')
                # self.entry_winer_show.pack(side='left')
                self.entry_winer_show.place(x=10, y=360)

                # rolling name
                self.rolling_name = tk.StringVar()
                self.rolling_name.set('    ')
                self.rolling_name_show = tk.Entry(self.window, font=('宋体', 28),textvariable=self.rolling_name, width=20)
                # self.rolling_name_show.pack(side='top')
                self.rolling_name_show.place(x=350, y=20)

                # rolling start/stop button
                self.on_hit = False
                self.hit_cnt = 0
                self.button_start_str = tk.StringVar()
                self.button_start_str.set('Start')

                self.btn_start = tk.Button(self.window, font=('Arial', 36),textvariable=self.button_start_str, command=self.rolling_start)
                self.btn_start.place(x=750, y=490)




        def rolling_start(self):

            if self.on_hit == False:
                self.hit_cnt = self.hit_cnt + 1 # click times
                self.on_hit = True

                self.button_start_str.set('Stop')
                self.start_thread()
            else:
                self.on_hit = False
                self.button_start_str.set('Start')
                self.stop_thread()
            pass

        def stop_thread(self):
                self.run_f = 0

        def start_thread(self):
                self.run_f = 1
                self.thread_1 = td.Thread(target=self.thread_test1)
                self.thread_1.start()
               

        def thread_test1(self):

                if len(self.employee_name_list) < int(self.winer_num.get()):

                    print('请输入小于%d的人数'%(len(self.employee_name_list)))
                    self.rolling_name.set('请输入小于%d的人数'%(len(self.employee_name_list)))
                    self.button_start_str.set('Start')
                    self.on_hit = False

                else:

                    self.employee_winers_num = int(self.winer_num.get())
                    # employee_winers_list = random.sample(self.employee_name_list, self.employee_winers_num)
                    # # for d in employee_winers_list:
                    # #     self.employee_name_list.remove(d)
                    # print("winer num %d" % self.employee_winers_num)

                    while self.run_f == 1:
                        emp_list_temp = random.sample(self.employee_name_list, len(self.employee_name_list))
                        employee_winers_list = emp_list_temp[0:self.employee_winers_num]


                        i = 0
                        for emp in emp_list_temp:

                            time.sleep(0.01)
                            employee_winers_list[i % self.employee_winers_num] = emp
                            self.rolling_name.set(emp)
                            i = i + 1

                            if self.run_f != 1:
                                print("exit rolling %d %d" % (self.hit_cnt,i))
                                self.rolling_name.set("大吉大利,恭喜恭喜")
                                break

                    winer_names = ''
                    #去掉已经中奖人员
                    for name in employee_winers_list:
                        self.employee_name_list.remove(name)
                        winer_names = winer_names + name[:-1] + ' '

                    print(winer_names)
            
                    self.winer_show.set(winer_names)

        def get_all_employee_name_from_file(self, file_name):

            self.employee_name_list.clear()
            #e_names_file = open(file_name, 'r', encoding='UTF-8')
            e_names_file = open(file_name, 'r')

            for emp1 in e_names_file:
                self.employee_name_list.append(emp1)

            e_names_file.close()

lucker = gunlun()
lucker.get_all_employee_name_from_file('Name1.csv')

lucker.window.mainloop()
