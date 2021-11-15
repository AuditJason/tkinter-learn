#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 22:39:21 2021

@author: jason
"""

import tkinter as tk
from tkinter import ttk
from get_swclass import SwClass
industry, industry_company= SwClass().swclass_all
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
tree = ttk.Treeview(window, show = "tree", selectmode='extended')
 
# myid=tree.insert("",0,"中国",text="中国China",values=("1"))  # ""表示父节点是根
# myidx1=tree.insert(myid,0,"广东",text="中国广东",values=("2"))  # text表示显示出的文本，values是隐藏的值
# myidx2=tree.insert(myid,1,"江苏",text="中国江苏",values=("3"))
# myidy=tree.insert("",1,"美国",text="美国USA",values=("4"))
# myidy1=tree.insert(myidy,0,"加州",text="美国加州",values=("5"))


def add_tree_data(treetable, data_dic, open=True):
    # 不继承父类add_data,而是重写
    '''
    data_dic = {'中国':['广州','北京','上海'],'美国':['纽约','华盛顿','洛杉矶']}
    '''
    for m, k in enumerate(data_dic.keys()):
        if not treetable.exists(k):  # 判断前期是否已添加一级条目
            treek = treetable.insert("", m, k, text=k, values=k, open=open)
        elif treetable.exists(k):
            treek = k
        if data_dic[k]:
            for n, i in enumerate(data_dic.get(k)):
                treetable.insert(treek, n, i, text=i, values=i)
                treek2 = i
                if type(data_dic[k]) == dict:
                    if data_dic.get(k).get(i):
                        for n2, i2 in enumerate(data_dic.get(k).get(i)):
                            treetable.insert(treek2, n2, i2, text=i2, values=i2)

add_tree_data(tree, industry, open=False)
tree.pack(expand = True, fill = tk.BOTH)
# 鼠标选中一行回调
def selectTree(event):
    #for item in tree.selection():
    #    item_text = tree.item(item, "values")
    print('*'*30)
    item = tree.selection()
    print(item, type(item))
    item_parent = tree.parent(item)
    print(item_parent, type(item_parent))
    item_parent_parent = tree.parent(item_parent)
    print(item_parent_parent, type(item_parent_parent))

def delete_tree():
    print('删除所有项目：')
    #tree.delete(tree.index('I000'))
    items = tree.get_children()
    print(items)
    for item in items:
        tree.delete(item)
    #tree.insert('','end',values=industry, )
     
# 选中行
tree.bind('<<TreeviewSelect>>', selectTree)
def btn2_change_t1():
    print(tree)
    tree.state='disable'
btn2 = tk.Button(window, text='TEST', fg="blue", state='normal', width=12, height=1, command=delete_tree)
btn2.pack()

 
window.mainloop()
