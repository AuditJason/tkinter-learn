# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 13:41:02 2021

@author: Administrator
"""
import tkinter as tk
from tkinter import ttk

class CreateTable:
    def __init__(self, index=True) -> None:
        self.__index = index

    def create_table(self, master, columns, heading, width, selectmode='extended', height=10):
        '''
        columns = ["name", "gender", "age"]\n
        heading = ['姓名', '性别', '年龄']\n
        rows = [["yang", "男", "18"], ["郑", "女", "25"]]\n
        '''
        if self.__index:
            columns.insert(0, "index")
            heading.insert(0, "序号")
            width.insert(0, 50)
        columns = columns  # 定义列的名称
        yscroll = tk.Scrollbar(master, orient=tk.VERTICAL)
        self.tree = ttk.Treeview(
            master,
            show="headings",
            columns=columns,
            selectmode=selectmode,
            height=height,
            yscrollcommand=yscroll.set)

        for c, h, w in zip(columns, heading, width):
            self.tree.column(c, width=w, anchor="center")  # 设置表格文字居中
            self.tree.heading(c, text=h)  # 设置表格头部标题
        yscroll.config(command=self.tree.yview)
        yscroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.tree.pack()

    def add_data(self, rows):
        for n, r in enumerate(rows):  # [[1,2],[2,3]]*2  使用此种方式的列表，r.insert(0, n+1)迭代出的数据不是预期
            if self.__index:
                r.insert(0, n+1)
                self.tree.insert('', n, values=tuple(r))  # 设置表格内容  n, r[0], r[1], r[2])
            else:
                self.tree.insert('', n, values=tuple(r))  # 设置表格内容  r[0], r[1], r[2]


    @property
    def selected_data(self):
        selection__d = []
        for item in self.tree.selection():
            item_text = self.tree.item(item, "values")
            selection__d.append(item_text)
        return selection__d

class CreateTree:

    def __init__(self, master, selectmode='extended',  height=10):
        yscroll = tk.Scrollbar(master, orient=tk.VERTICAL)
        self.__tree = ttk.Treeview(
            master,
            show='tree',
            selectmode=selectmode,
            height=height,
            yscrollcommand=yscroll.set)
        self.__tree.column(0, width=30)
        yscroll.config(command=self.__tree.yview)
        yscroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.__tree.pack()


    def add_data(self, data_dic):
        '''
        data_dic = {'中国':['广州','北京','上海'],'美国':['纽约','华盛顿','洛杉矶']}
        '''
        for m, k in  enumerate(data_dic.keys()):
            treek = self.__tree.insert("", m, k, text=k, values=k)
            for n, i in enumerate(data_dic[k]):
                self.__tree.insert(treek, n, i, text=i, values=i)

    #@property
    def selected_data(self):
        selection__d = []
        for item in self.__tree.selection():
            item_text = self.__tree.item(item, "values")
            selection__d.append(item_text)
        print(selection__d)
        return selection__d

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
window.title("TreeView-TreeClass参数说明")
# 设置窗口初始位置在屏幕居中
window.geometry("%sx%s+%s+%s" % (winWidth, winHeight, x, y))
# 设置窗口图标
# window.iconbitmap("./image/icon.ico")
# 设置窗口宽高固定
window.resizable(0, 0)

data_dic = {'中国':['广州','北京','上海'],'美国':['纽约','华盛顿','洛杉矶']}

tree = CreateTree(window)
tree.add_data(data_dic) 
tk.Button(window, text='确认', command=tree.selected_data).pack(side='bottom')
window.mainloop()






