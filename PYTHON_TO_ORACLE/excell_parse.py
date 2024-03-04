from tkinter import *
from tkinter.filedialog import *
from xlrd import*
root= Tk()
root.title('Загрузка таблиц')
root.geometry('610x160+300+300')
f = open('example.txt', 'w+')
def opfl(event):
    global op
    op=askopenfilename(filetypes=[('XLS','*.xls'),('XLSX','*.xlsx')])
    state.config(text='Выбран файл - '+op)


def loadfile(event):
    try:
        print('Модуль xlrd импортирован')
        state.config(text='Модуль xlrd импортирован')
    except ImportError:
        print('Ошибка импорта модуля xlrd')
        state.config(text='Ошибка импорта модуля xlrd')
    ex_dat = open_workbook(op)
    sheet = ex_dat.sheet_by_index(0)
    rown = sheet.nrows
    colln = sheet.ncols

    # Записываем данные
    for i in range(1, rown):
        z = "insert into " + str(tabl.get()) + " values ('"
        for j in range(0, colln):
            z += str(sheet.cell(i, j).value) + "','"
        z = z[:-2] + ");"
        #print(z)
        f.write(z+'\n')
        #thcur.execute(z)
        #thcur.execute('commit')
        state.config(text='Данные загружены')
    f.close()

#lab_user = Label (root,text='Введите логин')
#user = Entry(root,width=20)
#lab_pass = Label (root,text='Введите пароль')
#password = Entry(root,width=20, show = '*')



lab_tabl = Label (root,text='Таблица')
tabl = Entry(root,width=20)
state_text = Label (root,text='Статус:')
state = Label (root,text='')
flag_tbl = IntVar()
#flag_tbl_check = Checkbutton (root,text='Создать новую таблицу',variable=flag_tbl,onvalue=1,offvalue=0)
flag_date = IntVar()
#flag_date_check = Checkbutton (root,text='Перезаписать данные',variable=flag_date,onvalue=1,offvalue=0)

btn_load = Button (root,text='Импортировать',width=20,height=5,bg='white',fg='black')
btn_open = Button (root,text='Выбрать файл',width=20,height=5,bg='white',fg='black')
#btn_conn = Button (root,text='Подключение к БД',width=20,height=5,bg='white',fg='black')

btn_load.bind('<Button-1>',loadfile)
btn_open.bind('<Button-1>',opfl)
#btn_conn.bind('<Button-1>',conn)


#lab_user.grid(row=1,column=1)
#user.grid(row=1,column=2)
#lab_pass.grid(row=1,column=3)
#password.grid(row=1,column=4)
#flag_tbl_check.grid(row=2,column=3)
lab_tabl.grid(row=2,column=1)
tabl.grid(row=2,column=2)
#flag_date_check.grid(row=2,column=4)
state_text.grid(row=3,column=1)
state.grid(row=3,column=2)
#btn_conn.grid(row=4,column=1)
btn_open.grid(row=4,column=2)
btn_load.grid(row=4,column=3)
root.mainloop()
