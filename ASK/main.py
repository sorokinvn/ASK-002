#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
import datetime
import time
import threading
import tkinter as tk
from time import sleep
from tkinter import  messagebox
from tkinter import*

# объявляем класс GEP
class Gep():
    def __init__(self, name, x, y):
        self.name = name
        # координаты размещения виджета
        self.x = x
        self.y = y
        # уставки допустимых значений контролируемых параметров
        self.u_min = 207
        self.u_max = 253
        self.f_min = 49.6
        self.f_max = 50.4

    def creat(self):

        # создаем фрейм gep
        self.frame_gep = Frame(frame_root, width=540, height=200, relief=GROOVE, borderwidth=2)
        self.frame_gep.place(x=self.x, y=self.y)

        # рисуем картинку gep
        lb_image_gep = Label(self.frame_gep, image=image_gep, relief=RIDGE, borderwidth=2)
        lb_image_gep.place(x=5, y=5)

        # рисуем имя gep
        lb_name_gep = Label(self.frame_gep, width=9, text=self.name, font="Arial 12 bold",
                            bg='orange', relief=RIDGE, borderwidth=2)
        lb_name_gep.place(x=57, y=153)

        # рисуем поле статуса gep
        self.lb_status_gep = Label(self.frame_gep, width=12, font="Arial 12 bold",
                                   relief=RIDGE, borderwidth=2)
        self.lb_status_gep.place(x=160, y=153)

        # рисуем поля параметров gep
        lb_gep = Label(self.frame_gep, text='СЕТЬ ДЭС', width=12, font="Arial 8 bold",
                       relief=RIDGE, borderwidth=2)
        lb_gep.place(x=320, y=5)

        lb_ua_gep = Label(self.frame_gep, text='Ua, В', width=5, font="Arial 8 bold",
                          bg='orange', relief=RIDGE, borderwidth=2)
        lb_ua_gep.place(x=320, y=27)

        self.lb_ua_gep_value = Label(self.frame_gep, width=5, font="Arial 8 bold",
                                     relief=RIDGE, borderwidth=2)
        self.lb_ua_gep_value.place(x=369, y=27)

        lb_ub_gep = Label(self.frame_gep, text='Ub, В', width=5, font="Arial 8 bold",
                          bg='orange', relief=RIDGE, borderwidth=2)
        lb_ub_gep.place(x=320, y=49)

        self.lb_ub_gep_value = Label(self.frame_gep, width=5, font="Arial 8 bold",
                                     relief=RIDGE, borderwidth=2)
        self.lb_ub_gep_value.place(x=369, y=49)

        lb_uc_gep = Label(self.frame_gep, text='Uc, В', width=5, font="Arial 8 bold",
                          bg='orange', relief=RIDGE, borderwidth=2)
        lb_uc_gep.place(x=320, y=71)

        self.lb_uc_gep_value = Label(self.frame_gep, width=5, font="Arial 8 bold",
                                     relief=RIDGE, borderwidth=2)
        self.lb_uc_gep_value.place(x=369, y=71)

        lb_f_gep = Label(self.frame_gep, text='F, Гц', width=5, font="Arial 8 bold",
                         bg='orange', relief=RIDGE, borderwidth=2)
        lb_f_gep.place(x=320, y=93)

        self.lb_f_gep_value = Label(self.frame_gep, width=5, font="Arial 8 bold",
                                    relief=RIDGE, borderwidth=2)
        self.lb_f_gep_value.place(x=369, y=93)

        lb_sw_gep = Label(self.frame_gep, text='ПОЛОЖЕНИЕ ATyS', width=15, font="Arial 8 bold",
                          relief=RIDGE, borderwidth=2)
        lb_sw_gep.place(x=320, y=146)

        self.lb_sw_gep_value = Label(self.frame_gep, width=12, font="Arial 8 bold",
                                     relief=RIDGE, borderwidth=2)
        self.lb_sw_gep_value.place(x=440, y=146)

        lb_key_gep = Label(self.frame_gep, text='РЕЖИМ ATyS', width=15, font="Arial 8 bold",
                           relief=RIDGE, borderwidth=2)
        lb_key_gep.place(x=320, y=168)

        self.lb_key_gep_value = Label(self.frame_gep, width=12, font="Arial 8 bold",
                                      relief=RIDGE, borderwidth=2)
        self.lb_key_gep_value.place(x=440, y=168)

        # рисуем поля параметров вру
        lb_vru = Label(self.frame_gep, text='СЕТЬ ВРУ', width=12, font="Arial 8 bold",
                       relief=RIDGE, borderwidth=2)
        lb_vru.place(x=440, y=5)

        lb_ua_vru = Label(self.frame_gep, text='Ua, В', width=5, font="Arial 8 bold",
                          bg='sky blue', relief=RIDGE, borderwidth=2)
        lb_ua_vru.place(x=440, y=27)

        self.lb_ua_vru_value = Label(self.frame_gep, width=5, font="Arial 8 bold",
                                     relief=RIDGE, borderwidth=2)
        self.lb_ua_vru_value.place(x=489, y=27)

        lb_ub_vru = Label(self.frame_gep, text='Ub, В', width=5, font="Arial 8 bold",
                          bg='sky blue', relief=RIDGE, borderwidth=2)
        lb_ub_vru.place(x=440, y=49)

        self.lb_ub_vru_value = Label(self.frame_gep, width=5, font="Arial 8 bold",
                                     relief=RIDGE, borderwidth=2)
        self.lb_ub_vru_value.place(x=489, y=49)

        lb_uc_vru = Label(self.frame_gep, text='Uc, В', width=5, font="Arial 8 bold",
                          bg='sky blue', relief=RIDGE, borderwidth=2)
        lb_uc_vru.place(x=440, y=71)

        self.lb_uc_vru_value = Label(self.frame_gep, width=5, font="Arial 8 bold",
                                     relief=RIDGE, borderwidth=2)
        self.lb_uc_vru_value.place(x=489, y=71)

        lb_f_vru = Label(self.frame_gep, text='F, Гц', width=5, font="Arial 8 bold",
                         bg='sky blue', relief=RIDGE, borderwidth=2)
        lb_f_vru.place(x=440, y=93)

        self.lb_f_vru_value = Label(self.frame_gep, width=5, font="Arial 8 bold",
                                    relief=RIDGE, borderwidth=2)
        self.lb_f_vru_value.place(x=489, y=93)

    # задаем статус gep
    def set_status(self, status):
        self.status = status
        if self.status == 0:
            self.lb_status_gep.config(text='ОСТАНОВЛЕН', bg='gray99')
        if self.status == 1:
            self.lb_status_gep.config(text='РАБОТАЕТ', bg='spring green')

    # задаем значение ua gep
    def set_ua_gep(self, value):
        self.value = value
        self.lb_ua_gep_value.config(text=self.value)
        if self.value <= self.u_min or self.value >= self.u_max:
            self.lb_ua_gep_value.config(bg='red')
            if self.value == 0:
                self.lb_ua_gep_value.config(bg=root.cget('bg'))
        else:
            self.lb_ua_gep_value.config(bg='spring green')

    # задаем значение ub gep
    def set_ub_gep(self, value):
        self.value = value
        self.lb_ub_gep_value.config(text=self.value)
        if self.value <= self.u_min or self.value >= self.u_max:
            self.lb_ub_gep_value.config(bg='red')
            if self.value == 0:
                self.lb_ub_gep_value.config(bg=root.cget('bg'))
        else:
            self.lb_ub_gep_value.config(bg='spring green')

    # задаем значение uc gep
    def set_uc_gep(self, value):
        self.value = value
        self.lb_uc_gep_value.config(text=self.value)
        if self.value <= self.u_min or self.value >= self.u_max:
            self.lb_uc_gep_value.config(bg='red')
            if self.value == 0:
                self.lb_uc_gep_value.config(bg=root.cget('bg'))
        else:
            self.lb_uc_gep_value.config(bg='spring green')

    # задаем значение f gep
    def set_f_gep(self, value):
        self.value = value
        self.lb_f_gep_value.config(text=self.value)
        if self.value <= self.f_min or self.value >= self.f_max:
            self.lb_f_gep_value.config(bg='red')
            if self.value == 0:
                self.lb_f_gep_value.config(bg=root.cget('bg'))
        else:
            self.lb_f_gep_value.config(bg='spring green')

    # задаем положение ati
    def set_sw_pos(self, value):
        self.value = value
        if self.value == 2 or self.value == 9:
            self.lb_sw_gep_value.config(text='ВРУ')
        if self.value == 1 or self.value == 10:
            self.lb_sw_gep_value.config(text='0')
        if self.value == 3 or self.value == 36:
            self.lb_sw_gep_value.config(text='ДЭС')

    # задаем режим ati
    def set_key_pos(self, value, gep_type):
        self.value = value
        self.gep_type = gep_type
        if self.gep_type == 110:
            if self.value == 0:
                self.lb_key_gep_value.config(text='АВТО')
            if self.value == 4:
                self.lb_key_gep_value.config(text='РУЧНОЙ')
        if self.gep_type == 100 or self.gep_type == 33:
            if self.value == 0:
                self.lb_key_gep_value.config(text='РУЧНОЙ')
            if self.value == 16:
                self.lb_key_gep_value.config(text='АВТО')
            if self.value == 32:
                self.lb_key_gep_value.config(text='ПРОВЕРКА', bg='coral')
            if self.value == 64:
                self.lb_key_gep_value.config(text='ЗАПРЕТ', bg='coral')

    # задаем значение ua вру
    def set_ua_vru(self, value):
        self.value = value
        self.lb_ua_vru_value.config(text=self.value)
        if self.value <= self.u_min or self.value >= self.u_max:
            self.lb_ua_vru_value.config(bg='red')
        else:
            self.lb_ua_vru_value.config(bg='spring green')

    def set_ub_vru(self, value):
        self.value = value
        self.lb_ub_vru_value.config(text=self.value)
        if self.value <= self.u_min or self.value >= self.u_max:
            self.lb_ub_vru_value.config(bg='red')
        else:
            self.lb_ub_vru_value.config(bg='spring green')

    def set_uc_vru(self, value):
        self.value = value
        self.lb_uc_vru_value.config(text=self.value)
        if self.value <= self.u_min or self.value >= self.u_max:
            self.lb_uc_vru_value.config(bg='red')
        else:
            self.lb_uc_vru_value.config(bg='spring green')

    def set_f_vru(self, value):
        self.value = value
        self.lb_f_vru_value.config(text=self.value)
        if self.value <= self.f_min or self.value >= self.f_max:
            self.lb_f_vru_value.config(bg='red')
        else:
            self.lb_f_vru_value.config(bg='spring green')

def potok (my_func):
    def wapper(*args, **kwargs):
        my_thread = threading.Thread(target = my_func, args = args, kwargs = kwargs, daemon = True)
        my_thread.start()
    return wapper

@potok
def gtime():
    try:
        while True:
            lb_clock.config(text = datetime.datetime.now().strftime('%d-%m-%Y\n%H:%M:%S'))
            time.sleep(1)
    except:
        pass

@potok
def gep_100_get():
    try:
        while True:
            gep_100.set_ua_gep(random.randint(206, 254))
            gep_100.set_ub_gep(random.randint(206, 254))
            gep_100.set_uc_gep(random.randint(206, 254))
            gep_100.set_f_gep(random.randint(496, 504)/10)
            gep_100.set_ua_vru(random.randint(206, 254))
            gep_100.set_ub_vru(random.randint(206, 254))
            gep_100.set_uc_vru(random.randint(206, 254))
            gep_100.set_f_vru(random.randint(496, 504) / 10)
            time.sleep(.3)
    except:
        pass

@potok
def gep_110_get():
    try:
        while True:
            gep_110.set_ua_gep(random.randint(206, 254))
            gep_110.set_ub_gep(random.randint(206, 254))
            gep_110.set_uc_gep(random.randint(206, 254))
            gep_110.set_f_gep(random.randint(496, 504) / 10)
            gep_110.set_ua_vru(random.randint(206, 254))
            gep_110.set_ub_vru(random.randint(206, 254))
            gep_110.set_uc_vru(random.randint(206, 254))
            gep_110.set_f_vru(random.randint(496, 504) / 10)
            time.sleep(.3)
    except:
        pass

@potok
def gep_33_get():
    try:
        while True:
            gep_33.set_ua_gep(random.randint(206, 254))
            gep_33.set_ub_gep(random.randint(206, 254))
            gep_33.set_uc_gep(random.randint(206, 254))
            gep_33.set_f_gep(random.randint(496, 504) / 10)
            gep_33.set_ua_vru(random.randint(206, 254))
            gep_33.set_ub_vru(random.randint(206, 254))
            gep_33.set_uc_vru(random.randint(206, 254))
            gep_33.set_f_vru(random.randint(496, 504) / 10)
            time.sleep(.3)
    except:
        pass


# создаем главное окно программы
root = tk.Tk()
root.attributes('-fullscreen', True)
# порверяем текущее разрешение экрана, если не 1920 х 1080 - не запускаемся
if root.winfo_screenwidth() != 1920 or root.winfo_screenheight() != 1080:
    messagebox.showerror(message = 'Разрешение экрана не равно: 1920 x 1080' , title="Ошибка")
    root.destroy()
else:
    # создаем основной фрейм главного окна
    frame_root = Frame(root, width = 1910, height = 1070, relief = GROOVE, borderwidth = 2)
    frame_root.place(x = 5, y = 5)

    # создаем правый фрейм главного окна
    frame_button = Frame(frame_root, width=200, height=1055, relief=GROOVE, borderwidth=2)
    frame_button.place(x=1700, y=5)

    # рисуем часы
    lb_clock = Label(frame_button, font="Arial 18 bold", width=12, height=3, bg = 'dim gray',
                     fg = 'spring green', relief=RIDGE, borderwidth=2)
    lb_clock.place(x=5, y=5)

    # загружаем картинку GEP
    image_gep = PhotoImage(file = 'image/gep.png')

    gep_100 = Gep(name = 'GEP 100', x = 5, y = 5)
    gep_100.creat()
    gep_110 = Gep(name = 'GEP 110', x=5, y=220)
    gep_110.creat()
    gep_33 = Gep(name = 'GEP 33', x=5, y=435)
    gep_33.creat()

    gep_100.set_status(1)
    gep_100.set_key_pos(16, 100)
    gep_100.set_sw_pos(2)
    gep_100_get()

    gep_110.set_status(1)
    gep_110.set_key_pos(4, 110)
    gep_110.set_sw_pos(3)
    gep_110_get()

    gep_33.set_status(0)
    gep_33.set_key_pos(64, 100)
    gep_33.set_sw_pos(2)
    gep_33_get()

    gtime()
root.mainloop()
