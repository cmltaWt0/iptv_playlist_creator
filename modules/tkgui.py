# -*- coding: utf-8 -*-

import os
from xlrd import open_workbook
import codecs
from Tkinter import Tk, Menu, END, Toplevel, Label, Frame, Entry, Button, WORD, Text
import tkFileDialog

'''
Created on 23.12.2011

@author: maksim
'''

sheet0 = 0
open_file = ''
tmp = 'tmp/tmp_file.txt'


def parse (row_num):
    '''
    Readig row-num row in EXCEL file
    '''
    _list = []
    item = sheet0.row_values(row_num, 0, 3) #reading 3 col (0,1,2) in row_num row
    for i in item:
        _list.append(i)
    return _list

def iter_write_section(_list):
    '''
    Writing some repeated text
    '''
    tex.insert(END, '\n')
    for i in _list:
        tex.insert(END, i)
    tex.insert(END,'\n')   

def transformation(event):
    '''
    Action of Transform button - invoking iter_write() and parse() func
    '''
    _list = []
    if open_file:    
        book = open_workbook(open_file) #reading opened file to XML parser
    
        global sheet0
        sheet0 = book.sheet_by_index(0) #init sheet0
   
        tex.delete(1.0,END) #erasing previous text in tex area
        tex.insert(END, '#EXTM3U\n')
  
        first_row = 7
   
        if ent1.get():
            i = 1
            num = first_row #first row of group
            while i <= int(ent1.get()): #count of channels in group
                _list = parse(num-1) #reading num's row in sheet0
                if _list[1] < 10 and _list[1] > 0:
                    list2 = '#EXTINF:0,00'
                elif _list[1] > 99:
                    list2 = '#EXTINF:0,'
                else:
                    list2 = '#EXTINF:0,0'
                a = _list[0]
                string = a.encode('utf-8')
                list2 += str(int(_list[1])) + ' ' + '[' + 'SOCIAL' + ']' + ' ' + string + '\n' + 'udp://@' 
                list2 += str(_list[2]) + ':5004'
                iter_write_section(list2)
                i += 1
                num += 1

        if ent2.get():
            i = 1
            num = first_row + int(ent1.get()) + 2
            while i <= int(ent2.get()):
                _list = parse(num-1)
                if _list[1] < 10 and _list[1] > 0:
                    list2 = '#EXTINF:0,00'
                elif _list[1] > 99:
                    list2 = '#EXTINF:0,'
                else:
                    list2 = '#EXTINF:0,0'
                list2 += str(int(_list[1])) + ' ' + '[' + 'BASE' + ']' + ' ' + _list[0] + '\n' + 'udp://@'
                list2 += str(_list[2]) + ':5004'
                iter_write_section(list2)
                i += 1
                num += 1
        if ent3.get():
            i = 1
            num = first_row + int(ent1.get()) + int(ent2.get()) + 4
            while i <= int(ent3.get()):
                _list = parse(num-1)
                if _list[1] < 10 and _list[1] > 0:
                    list2 = '#EXTINF:0,00'
                elif _list[1] > 99:
                    list2 = '#EXTINF:0,'
                else:
                    list2 = '#EXTINF:0,0'
                list2 += str(int(_list[1])) + ' ' + '[' + 'FULL' + ']' + ' ' + _list[0] + '\n' + 'udp://@'
                list2 += str(_list[2]) + ':5004'
                iter_write_section(list2)
                i += 1
                num += 1
    
        letter = tex.get(1.0,END)
        f = codecs.open('tmp/tmp_file.txt', "w", "utf-8")
        f.write(letter)
        f.close()
    
    else:
        tex.delete(1.0,END)
        tex.insert(END,'Сначала откройте исходный файл xls')

def mail_source(event):
    '''
    Sending EXCEL(source) file
    '''
    from modules.send_mail import send_mail
    from modules.conf_fetcher import fetcher
  
    a = fetcher() #take a dict with conf setting
    if open_file:
        a ['files'] = [open_file]
 
    send_mail(**a)

    tex.delete(1.0,END)
    tex.insert(END,'Файл ')
    tex.insert(END, open_file)
    tex.insert(END, ' отправлен')

def mail_result(event):
    '''
    Sending TXT(result) file
    '''
    from modules.send_mail import send_mail
    from modules.conf_fetcher import fetcher

    a = fetcher() #take a dict with conf setting
    
    a ['files'] = [tmp]

    send_mail(**a)

    tex.delete(1.0, END)
    tex.insert(END, 'Результат сохранен во временный файл ')
    tex.insert(END, 'tmp/tmp_file.txt')
    tex.insert(END, ' и отправлен по почте')

def _open():
    '''
    Opening EXCEL source file
    '''
    global open_file
    open_file = tkFileDialog.askopenfilename()
    filename = os.path.basename(open_file)
    tex.delete(1.0,END)
    tex.insert(END,'Открыт файл ')
    tex.insert(END, filename)
    tex.insert(END, '.\nТеперь введите день, для которого будет выполнено преобразование')

def _save():
    '''
    Saving result TXT file
    '''
    sa = tkFileDialog.asksaveasfilename()
    letter = tex.get(1.0,END)
    f = codecs.open(sa, "w", "utf-8")
    f.write(letter)
    f.close()

def _close():
    root.destroy()

def _help():
    win = Toplevel(root)
    lab = Label(win, text="Вам необходимо ввести колличество каналов в пакетах Социальный, Базовый и Полный.\nПосле этого открыть EXCEL файл с нужным сервичным планом и нажать на кнопку Преобразовать.\nРезультат будет преобразован в формат txt\nи появится на экране. Файл txt будет автоматически сохранен.")
    lab.pack()

def _about():
    win = Toplevel(root)
    lab = Label(win, text="Эта программа преобразовывает xls файл \n в txt формат специальной разметкой.")
    lab.pack()


root = Tk()

root.title('IPTV playlist creator')
m = Menu(root)
root.config(menu=m)
fm = Menu(m)
m.add_cascade(label="File", menu=fm)
fm.add_command(label="Open", command = _open)
fm.add_command(label="Save", command = _save)
fm.add_command(label="Exit", command = _close)

hm = Menu(m)
m.add_cascade(label="Help", menu=hm)
hm.add_command(label="Help", command = _help)
hm.add_command(label="About", command = _about)

fra1 = Frame(root, width=500, height=30, bd = 5)
fra2 = Frame(root, width=500, height=100, bd = 5)
fra3 = Frame(root, width=500, height=500, bd = 5)
 
lab1 = Label(fra1, text="Колличество каналов в пакете Социальный")
lab2 = Label(fra1, text="Колличество каналов в пакете Базовый")
lab3 = Label(fra1, text="Колличество каналов в пакете Полный")
ent1 = Entry(fra1, width=4)
ent2 = Entry(fra1, width=4)
ent3 = Entry(fra1, width=4)
but1 = Button(fra1, text = "Преобразовать")
but2 = Button(fra3, text = "Отправить исходник")
but3 = Button(fra3, text = "Отправить результат")
tex = Text(fra2, width=60, height=12, font="12", wrap=WORD)
 
lab1.grid(row = 0, column = 0)
lab2.grid(row = 1, column = 0)
lab3.grid(row = 2, column = 0)
ent1.grid(row = 0, column = 1, padx=20)
ent2.grid(row = 1, column = 1, padx=20)
ent3.grid(row = 2, column = 1, padx=20)
but1.grid(row = 3, column = 1, padx=20)
tex.grid(row = 0, column = 0)
but2.grid(row = 0, column = 1)
but3.grid(row = 1, column = 1)
 
fra1.pack()
fra2.pack()  
fra3.pack()
but1.bind("<Button-1>", transformation)
but2.bind("<Button-1>", mail_source)
but3.bind("<Button-1>", mail_result)
   
root.mainloop()