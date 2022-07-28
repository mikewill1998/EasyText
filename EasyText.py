import os
import tkinter as tk
from tkinter import *
from tkinter import filedialog, colorchooser, font, messagebox
from tkinter.filedialog import *


# -------------------------
def save_new_file():
    file = filedialog.asksaveasfilename(initialfile="untitled",
                                        defaultextension=".txt",
                                        filetypes=[("All files", "*"),
                                                   ("Text file", ".txt"),
                                                   ("Python document", ".py")])

    if file is None:
        return
    else:
        try:
            window.title(os.path.basename(file))
            fh = open(file, 'w')
            fh.write(text_area.get(1.0, END))
        except Exception:
            print("Can not save this file")
        else:
            fh.close()
    window.title("Untitled")
    text_area.delete(1.0, END)


def new_file():
    if messagebox.askyesno(title="Save file?", message="Do you want to save current file?"):
        save_new_file()
        window.title("Untitled")
        text_area.delete(1.0, END)
    else:
        window.title("Untitled")
        text_area.delete(1.0, END)


def open_file():
    file = askopenfilename(defaultextension=".txt",
                           filetypes=(("All files", "*"), ("text file", ".txt"), ("Python document", ".py")))
    try:
        window.title(os.path.basename(file))
        text_area.delete(1.0, END)
        fh = open(file, 'r')
        text_area.insert(1.0, fh.read())
    except Exception:
        print('Warning', "Could not open this file:")
    else:
        fh.close()


def leave():
    result = messagebox.askyesnocancel(title="Save file?", message="Do you want to save current file?")
    if (result == True):
        save_new_file()
        window.destroy()
    elif (result == False):
        window.destroy()
    else:
        print("Let me think")


# -------------------------
def cut():
    text_area.event_generate("<<Cut>>")


def copy():
    text_area.event_generate("<<Copy>>")


def paste():
    text_area.event_generate("<<Paste>>")


# -------------------------
def about():
    about_window = tk.Toplevel()
    about_window.title("Licence")
    about_window_width = 500
    about_window_height = 400
    about_screen_width = about_window.winfo_screenwidth()
    about_screen_height = about_window.winfo_screenheight()
    z = int((about_screen_width / 2) - (about_window_width / 2))
    w = int((about_screen_height / 2) - (about_window_height / 2))
    about_window.geometry("{}x{}+{}+{}".format(about_window_width, about_window_height, z, w))
    licence = Label(about_window, text="""MIT License Copyright (c) 2022 Cheng-Wei Liu

Permission is hereby granted, free of charge,
to any person obtaining a copy of this software and
associated documentation files (the "Software"),
to deal in the Software without restriction,
including without limitation the rights to use,
copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom
the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included
in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR
PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS
OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH
THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.""")
    licence.pack()


def setting():
    setting_window = tk.Toplevel()
    setting_window.title('Preference')
    frame = Frame(setting_window)
    frame.grid()
    color_label = Label(frame, text='Color')
    color_label.grid(row=0, column=0)
    color_btn = Button(frame, text="Color", command=change_color)
    color_btn.grid(row=0, column=1)
    font_label = Label(frame, text='Font')
    font_label.grid(row=1, column=0)
    font_box = OptionMenu(frame, font_name, *font.names(), command=change_font)
    font_box.grid(row=1, column=1)
    size_label = Label(frame, text='Size')
    size_label.grid(row=2, column=0)
    size_box = Spinbox(frame, from_=1, to=150, textvariable=font_size, command=change_font)
    size_box.grid(row=2, column=1)


def change_color():
    color = colorchooser.askcolor(title='Pick a color')
    text_area.config(fg=color[1])


def change_font(*args):
    text_area.config(font=(font_name.get(), font_size.get()))


# -------------------------

window = tk.Tk()
window.title("EasyText")

window_width = 600
window_height = 600
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))
window.geometry("{}x{}+{}+{}".format(window_width, window_height, x, y))

# -------------------------

font_name = StringVar(window)
font_name.set("TkDefaultFont")
font_size = StringVar(window)
font_size.set("25")

# -------------------------

text_area = Text(window, font=(font_name.get(), font_size.get()))
scroll_bar = Scrollbar(text_area)
scroll_bar.pack(side=RIGHT, fill=Y)

window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)
text_area.grid(sticky=N+S+E+W)
text_area.config(yscrollcommand=scroll_bar.set, fg='black')

# -------------------------

menu_bar = Menu(window)
window.config(menu=menu_bar)
file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New file", command=new_file)
file_menu.add_command(label="Open file", command=open_file)
file_menu.add_command(label="Save as", command=save_new_file)
file_menu.add_separator()
file_menu.add_command(label="Quit", command=leave)

editMenu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Cut", command=cut)
editMenu.add_command(label="Copy", command=copy)
editMenu.add_command(label="Paste", command=paste)

help_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='Help', menu=help_menu)
help_menu.add_command(label='About', command=about)
help_menu.add_command(label='Preference', command=setting)

# -------------------------

window.mainloop()
