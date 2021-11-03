#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 06:55:15 2021

@author: jason
"""

import tkinter as tk
from tkinter import ttk


class CreateFinanceRatio:
    def __init__(self, master, text):
        self.__ratio_var = tk.IntVar()
        ckb = tk.Checkbutton(master, text=text, variable=self.__ratio_var, onvalue=1, offvalue=0,)
        ckb.pack(side="left")
        self.__spinbox_start_var = tk.IntVar()
        sp1 = tk.Spinbox(master, textvariable=self.__spinbox_start_var, from_=0, to=1, width=4)
        sp1.pack(side="left")
        tk.Label(master, text='~').pack(side="left")
        self.__spinbox_end_var = tk.IntVar()
        sp2 = tk.Spinbox(master, textvariable=self.__spinbox_end_var, from_=0, to=1, width=4)
        sp2.pack(side="left")

    @property
    def checked_ratio(self):
        return self.__ratio_var.get(), self.__spinbox_start_var.get(), self.__spinbox_end_var.get()

window = tk.Tk()
# 设置窗口大小
winWidth = 600
winHeight = 400
# 获取屏幕分辨率
screenWidth = window.winfo_screenwidth()
screenHeight = window.winfo_screenheight()
 
x = int((screenWidth - winWidth) / 2)
y = int((screenHeight - winHeight) / 2)
 
# 设置主窗口标题
window.title("TreeView参数说明")
# 设置窗口初始位置在屏幕居中
window.geometry("%sx%s+%s+%s" % (winWidth, winHeight, x, y))
# 设置窗口图标
# window.iconbitmap("./image/icon.ico")
# 设置窗口宽高固定
window.resizable(0, 0)
 
# 定义列的名称
columns = ("name", "gender", "age")
tree = ttk.Treeview(window, show = "headings", columns = columns, selectmode = tk.BROWSE)
 
# 设置表格文字居中
tree.column("name", anchor = "center")
tree.column("gender", anchor = "center")
tree.column("age", anchor = "center")
 
# 设置表格头部标题
tree.heading("name", text = "姓名")
tree.heading("gender", text = "性别")
tree.heading("age", text = "年龄")
 
# 设置表格内容
lists = [{"name": "yang", "gender": "男", "age": "18"}, {"name": "郑", "gender": "女", "age": "25"}]
i = 0
for v in lists:
    tree.insert('', i, values = (v.get("name"), v.get("gender"), v.get("age")))
    i += 1
 
tree.pack(expand = True, fill = tk.BOTH)

def open_edit_window(event):
    item = tree.selection()
    item_text = tree.item(item, "values")
    print(item_text)
    print(type(item_text))
    if item:
        new_window = tk.Toplevel(window)
        winWidth, winHeight, x, y = 300, 182 , 500 ,500
        new_window.geometry("%sx%s+%s+%s" % (winWidth, winHeight, x, y))
        CFR = CreateFinanceRatio(new_window,item_text[0])
        tk.Button(new_window, text='确认', command=cahnge_ratio(item, )).pack()
 
# 获取当前点击行的值
def treeviewClick(event):  # 单击
    for item in tree.selection():
        item_text = tree.item(item, "values")
        print(item_text)

def get_focus(event):
    tree.focus(item=tree.selection())

def cahnge_ratio(item, values=CFR.checked_ratio):
    tree.item(item, text="blub", values=values)

def tree_edit(event):
    # 选择后修改选择项
    item = tree.selection()
    tree.item(item, text="blub", values=("jack", "foo", "bar"))

# 鼠标点击时开启新窗口，并提供修改项目，获取数据后修改原数据

# 鼠标左键抬起
# tree.bind('<ButtonRelease-1>', treeviewClick)  # 选择并获取数据
# tree.bind('<ButtonRelease-1>', get_focus)  # 修改数据
tree.bind('<ButtonRelease-1>', open_edit_window)  # 修改数据

 
# 鼠标选中一行回调
def selectTree(event):
    for item in tree.selection():
        item_text = tree.item(item, "values")
        print(item_text)
     
# 选中行
#tree.bind('<<TreeviewSelect>>', selectTree)
 
window.mainloop()