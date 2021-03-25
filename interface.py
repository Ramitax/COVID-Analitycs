from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from analyzer import Covid

class Interface(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.window = master

    def execute_interface(self):
        self.__configurate_window()
        self.__configurate_frame()
        self.__configurate_button()
        self.window.destroy()

    def __configurate_window(self):
        self.window.title("Covid Analyzer")
        self.window.resizable(False, False)

    def __configurate_frame(self):
        self.frame = Frame(self.window, bg="#232323", width='400', height='100', bd=10)
        self.frame.pack()
        Label(self.frame, text='Esto puede tardar aproximadamente 1 minuto', font=('@Microsoft YaHei UI', 11), fg="#cce7e8", bg="#232323").place(x=15, y=25)

    def __open_file(self):
        archive = filedialog.askopenfilename(title="Open file")
        try:
            app = Covid(str(archive))
            app.start()
        except:
            messagebox.showerror(title="Error", message="Recolect csv for: \nhttps://datos.gob.ar/")

    def __configurate_button(self):
        button = Button(self.frame, text="Open file", command=self.__open_file())