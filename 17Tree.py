# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 16:23:00 2021

@author: Administrator
"""
import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title('my window')

# 窗口尺寸
window.geometry('500x300')

tree = ttk.Treeview(window, columns=('size', 'modified', 'owner'))
tree.pack()

# 显示主窗口
window.mainloop()

