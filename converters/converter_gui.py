import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo

# create the root window
# root = tk.Tk()
# root.title('Tkinter Open File Dialog')
# root.resizable(False, False)
# root.geometry('300x150')
#
#
# def select_file():
#     filetypes = (
#         ('text files', "*.pdf"),
#         ('All files', '*.*')
#     )
#
#     filename = fd.askopenfilename(
#         title='Open a file',
#         initialdir='/',
#         filetypes=filetypes)
#
#     showinfo(
#         title='Selected File',
#         message=filename
#     )
#
#
# # open button
# open_button = ttk.Button(
#     root,
#     text='Open a File',
#     command=select_file
# )
#
# open_button.pack(expand=True)
#
#
# # run the application
# root.mainloop()


# class ConverterUI:
#
#     def __init__(self):
#         self._root = tk.Tk()
#
#     def set_title(self):
#         return self._root.title("Converter Interface")
#
#     def set_geometry(self, x, y):
#         self._root.geometry(f"{x}x{y}")
#
#     def open_ui(self):
#         self._root.mainloop()
#
#
# c = ConverterUI()
# c.set_title()
# c.set_geometry(400, 300)
# c.open_ui()

# create the root window
# root = tk.Tk()
# root.title('Tkinter File Dialog')
# root.resizable(False, False)
# root.geometry('300x150')


import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd

# Root window
root = tk.Tk()
root.title('Display a Text File')
root.resizable(False, False)
root.geometry('550x250')

# Text editor
text = tk.Text(root, height=12)
text.grid(column=0, row=0, sticky='nsew')


def open_text_file():
    # file type
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )
    # show the open file dialog
    f = fd.askopenfile(filetypes=filetypes)
    # read the text file and show its content on the Text
    text.insert('1.0', f.readlines())


# open file button
open_button = ttk.Button(
    root,
    text='Open a File',
    command=open_text_file
)

open_button.grid(column=0, row=1, sticky='w', padx=10, pady=10)


root.mainloop()
