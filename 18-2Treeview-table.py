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
        # self.__text_var = tk.IntVar()
        tk.Label(master, text='修改财务指标/比例，确认后确认作为筛选条件：').pack(side='top', anchor='w')
        self.text = text + ' :   '
        ckb = tk.Label(master, text=self.text)
        ckb.pack(side="left")
        self.__entry_start_var = tk.IntVar()
        sp1 = tk.Entry(master, textvariable=self.__entry_start_var, width=12)
        sp1.pack(side="left")
        tk.Label(master, text='      ~      ').pack(side="left")
        self.__entry_end_var = tk.IntVar()
        sp2 = tk.Entry(master, textvariable=self.__entry_end_var, width=12)
        sp2.pack(side="left")
        tk.Label(master, text='      ').pack(side='left')

    @property
    def checked_ratio(self):
        return self.text.split(' ')[0], self.__entry_start_var.get(), self.__entry_end_var.get()

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
tree = ttk.Treeview(window, show = "headings", columns = columns, selectmode = tk.EXTENDED)#tk.BROWSE
 
# 设置表格文字居中
tree.column("name", anchor = "center")
tree.column("gender", anchor = "center")
tree.column("age", anchor = "center")
 
# 设置表格头部标题
tree.heading("name", text = "姓名")
tree.heading("gender", text = "性别")
tree.heading("age", text = "年龄")
 
# 设置表格内容
lists = [{"name": "yang", "gender": "男", "age": "18"}, {"name": "性别性别性别性别性别", "gender": "女", "age": "25"}]*3
i = 0
for v in lists:
    tree.insert('', i, values = (v.get("name"), v.get("gender"), v.get("age")))
    i += 1
 
tree.pack()  # expand = True, fill = tk.BOTH



def open_edit_window(event):
    item = tree.selection()
    item_text = tree.item(item, "values")
    print(item_text)
    if item:
        new_window = tk.Toplevel(window)
        new_window.title('筛选参数修改')
        winWidth, winHeight, x, y = 500, 80 , 300 ,300
        new_window.geometry("%sx%s+%s+%s" % (winWidth, winHeight, x, y))
        new_window.resizable(False, False)
        CFR = CreateFinanceRatio(new_window,item_text[0])
        tk.Button(
            new_window,
            text='确认',
            command=lambda: (cahnge_ratio(item,  CFR.checked_ratio), new_window.destroy()),
        ).pack(side='left')
 
# 获取当前点击行的值
def treeviewClick(event):  # 单击
    for item in tree.selection():
        item_text = tree.item(item, "values")
        print(item_text)

def get_focus(event):
    tree.focus(item=tree.selection())

def cahnge_ratio(item, values):
    tree.item(item, values=values)

def tree_edit(event):
    # 选择后修改选择项
    item = tree.selection()
    tree.item(item, text="blub", values=("jack", "foo", "bar"))

# 鼠标点击时开启新窗口，并提供修改项目，获取数据后修改原数据

# 鼠标左键抬起
# tree.bind('<ButtonRelease-1>', treeviewClick)  # 选择并获取数据
# tree.bind('<ButtonRelease-1>', get_focus)  # 修改数据
# tree.bind('<ButtonRelease-1>', open_edit_window)  # 修改数据

 
# 鼠标选中一行回调
selection__data = []
def selectTree(event):
    for item in tree.selection():
        item_text = tree.item(item, "values")
        selection__data.append(item_text)
        print(item_text)

def delete_item():
    for item in tree.selection():
        tree.delete(item)

def get_selection():
    selection__d = []
    for item in tree.selection():
        item_text = tree.item(item, "values")
        selection__d.append(item_text)
    print(selection__d)

def get_all_data():
    root_items = tree.get_children()
    print(root_items)
    for item in root_items:
        # print(tree.get_children(item))  #
        print(tree.item(item)["values"])


# 选中行
tree.bind('<<TreeviewSelect>>', selectTree)
# tree.bind('<<TreeviewSelect>>', get_selection)
tk.Button(window, text='确认', command=get_all_data).pack(side='bottom')  # #tk.BOTTOM  #
 
window.mainloop()