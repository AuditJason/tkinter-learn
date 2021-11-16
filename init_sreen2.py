# coding=utf-8
from tkinter import * 
from tkinter import ttk 
import os 
import time 
import tkinter.font as tkFont 
import threading 
 
def showWelcome(): 
    sw = root.winfo_screenwidth() 
    #得到屏幕宽度 
    sh = root.winfo_screenheight() 
    #得到屏幕高度 
    root.overrideredirect(True) 
    root.attributes("-alpha", 1)#窗口透明度（1为不透明，0为全透明） 
    x=(sw-475)/2 
    y=(sh-200)/2 
    #设置窗口位于屏幕中部 
    root.geometry("475x200+%d+%d" %(x,y)) 
    root['bg']='black' 
    #插入欢迎图片，可以是logo 
    if os.path.exists('./Lib/img/welcome.png'): 
      print("Lib/img exist") 
      bm = PhotoImage(file = './Lib/img/welcome.png') 
      lb_welcomelogo = Label(root, image = bm,bg='black') 
      lb_welcomelogo.bm = bm 
      lb_welcomelogo.place(x=0, y=10,) 
    #插入文字，可以显示开发者或出处 
    lb_welcometext = Label(root, text = 'Welcome to use Long_xu application', 
         fg='lightgray',bg='black',font=('华文隶书', 22)) 
    lb_welcometext.place(x=0, y=91,width=475,height=100) 
 
def closeWelcome(): 
    #设置欢迎页停留时间 
    for i in range(2): 
      rootMSCT.attributes("-alpha", 0)#窗口透明度 
      time.sleep(1) 
    rootMSCT.attributes("-alpha", 1)#窗口透明度 
    root.destroy() 
rootMSCT= Tk()  #创建应用程序主窗口 
rootMSCT.title("Long_xu welcome v1.0"); 
rootMSCT.attributes("-alpha", 0) #透明状态下加载主程序 


msw = rootMSCT.winfo_screenwidth() 
msh = rootMSCT.winfo_screenheight() 
m_x=(msw-600)/2 
m_y=(msh-430)/2 
rootMSCT.geometry("600x430+%d+%d" %(m_x,m_y)) 
global root 
#创建欢迎界面窗口 
root = Toplevel() 
tMain=threading.Thread(target=showWelcome) 
tMain.start();
t1=threading.Thread(target=closeWelcome) 
t1.start(); 
''' 
主窗口程序代码 
''' 
time.sleep(10) 
rootMSCT.mainloop() 
