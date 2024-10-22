import tkinter as tk
from tkinter import filedialog, messagebox

def new_file():
    text_area.delete(1.0, tk.END)
    window.title("Новый файл - Блокнот")

def open_file():
    file = filedialog.askopenfilename(defaultextension=".txt",
                                      filetypes=[("Текстовые файлы", "*.txt"), ("Все файлы", "*.*")])
    if file:
        window.title(f"{file} - Блокнот")
        with open(file, "r", encoding="utf-8") as f:
            text_area.delete(1.0, tk.END)
            text_area.insert(tk.END, f.read())

def save_file():
    file = filedialog.asksaveasfilename(defaultextension=".txt",
                                        filetypes=[("Текстовые файлы", "*.txt"), ("Все файлы", "*.*")])
    if file:
        with open(file, "w", encoding="utf-8") as f:
            f.write(text_area.get(1.0, tk.END))
        window.title(f"{file} - Блокнот")

def exit_app():
    if messagebox.askokcancel("Выход", "Вы уверены, что хотите выйти?"):
        window.quit()

window = tk.Tk()
window.title("Простой блокнот")
window.geometry("600x400")

menu_bar = tk.Menu(window)
window.config(menu=menu_bar)

file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Файл", menu=file_menu)
file_menu.add_command(label="Новый", command=new_file)
file_menu.add_command(label="Открыть", command=open_file)
file_menu.add_command(label="Сохранить", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Выход", command=exit_app)

text_area = tk.Text(window, wrap="word")
text_area.pack(expand=True, fill="both")

window.mainloop()
