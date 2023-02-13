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


class ConverterUI:

    def __init__(self):
        self._root = tk.Tk()

    def set_title(self):
        return self._root.title("Converter Interface")

    def set_geometry(self, x, y):
        self._root.geometry(f"{x}x{y}")

    def open_ui(self):
        self._root.mainloop()


c = ConverterUI()
c.set_title()
c.set_geometry(400, 300)
c.open_ui()
