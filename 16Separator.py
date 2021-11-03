# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 13:57:29 2021

@author: Administrator
"""

import tkinter as tk
from tkinter import ttk 
root = tk.Tk()
root.geometry('320x240')
s=ttk.Style()
s.configure('red.TSeparator',background='red')
b=ttk.Separator(root,orient='horizontal',
                style='red.TSeparator')
a=ttk.Button(root,text='Button')
a.pack()
b.pack(fill=tk.X)
root.mainloop()
