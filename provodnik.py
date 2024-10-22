import tkinter
from tkinter import filedialog, messagebox
import os

def file_select():
    filename = filedialog.askopenfilename(initialdir='/', title='выберите файл',
                                          filetypes=(('текстовый файл', 'txt'), ('все файлы', '*')))
    text['text'] = text['text'] + ' ' + filename
    os.startfile(filename)

def show_info():
    info_message = (
        "Программа для выбора и открытия файлов.\n"
        "Нажмите 'выбрать файл', чтобы выбрать файл из системы, "
        "и он будет открыт с помощью приложения по умолчанию."
    )
    messagebox.showinfo("Info", info_message)

def show_about():
    about_message = "Автор: Kunigunda Production\nВерсия: V1_2_3"
    messagebox.showinfo("About", about_message)

window = tkinter.Tk()
window.title('Проводник')
window.geometry('350x350')
window.configure(bg='black')
window.resizable(False, False)

menu_bar = tkinter.Menu(window)
window.config(menu=menu_bar)

help_menu = tkinter.Menu(menu_bar, tearoff=0)
help_menu.add_command(label="Info", command=show_info)
help_menu.add_command(label="About", command=show_about)
menu_bar.add_cascade(label="Help", menu=help_menu)

text = tkinter.Label(window, text='Файл', height=5, width=25, background='silver', foreground='blue')
text.grid(column=1, row=1)

button_select = tkinter.Button(window, width=20, height=3, text='Выбрать файл', background='silver',
                               foreground='blue', command=file_select)
button_select.grid(column=1, row=2, pady=5)
window.mainloop()
