import tkinter as tk
import time
import random
import threading as td


class gunlun:

        employee_name_list = []
        employee_winers_num = 1 # the NUB of each level winer

        def __init__(self):
                self.run_f = 0

                # create windown
                self.window = tk.Tk()
                self.window.title('nian hui')
                self.window.geometry('1024x800')
                # self.window.configure(bg='#778899')
                self.window.resizable(width=False, height=False)

                # how many winer get
                self.winer_num_lable = tk.Label(self.window, text='winer num:', font=('Arial', 14), width=10, height=1)
                self.winer_num_lable.place(x=710, y=435)

                self.winer_num = tk.StringVar()
                self.winer_num.set('1')
                self.entry_winer_num = tk.Entry(self.window, width=5, font=('Arial', 14), textvariable=self.winer_num,)
                self.entry_winer_num.place(x=850, y=435)

                # show final winer
                self.winer_name_lable = tk.Label(self.window, text='Winer:', font=('Arial', 20), width=5, height=1)
                self.winer_name_lable.place(x=10, y=310)

                self.winer_show = tk.StringVar()
                self.winer_show.set('      ')
                self.entry_winer_show = tk.Entry(self.window, font=('Arial', 20), textvariable=self.winer_show, width=30)
                # self.entry_winer_show.pack(side='left')
                self.entry_winer_show.place(x=10, y=360)

                # rolling name
                self.rolling_name = tk.StringVar()
                self.rolling_name.set('gun dong kuang')
                self.rolling_name_show = tk.Entry(self.window, font=('Arial', 36),textvariable=self.rolling_name, width=15)
                # self.rolling_name_show.pack(side='top')
                self.rolling_name_show.place(x=350, y=20)

                # rolling start/stop button
                self.on_hit = False
                self.hit_cnt = 0
                self.button_start_str = tk.StringVar()
                self.button_start_str.set('Start')

                self.btn_start = tk.Button(self.window, font=('Arial', 36), textvariable=self.button_start_str, command=self.rolling_start)
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

                self.employee_winers_num = int(self.winer_num.get())
                employee_winers_list = random.sample(self.employee_name_list, self.employee_winers_num)
                print("winer num %d" % self.employee_winers_num)

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
                            self.rolling_name.set("Congratulations")
                            break

                winer_names = ''
                for name in employee_winers_list:
                    winer_names = winer_names + name[:-1] + ' '

                print(winer_names)
                self.winer_show.set(winer_names)

        def get_all_employee_name_from_file(self, file_name):

            self.employee_name_list.clear()
            e_names_file = open(file_name, 'r', encoding='UTF-8')

            for emp1 in e_names_file:
                self.employee_name_list.append(emp1)

            e_names_file.close()

lucker = gunlun()
lucker.get_all_employee_name_from_file('Name1.csv')

lucker.window.mainloop()
