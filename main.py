from interface import Interface
import tkinter as tk

root = tk.Tk()
app = Interface(master=root)
app.execute_interface()
app.mainloop()