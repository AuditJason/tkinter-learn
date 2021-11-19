from tkinter import *

top = Tk()

top.geometry("200x200")

spin = Spinbox(top, values=('a','b'))#from_=0, to=25)

spin.pack()

top.mainloop()