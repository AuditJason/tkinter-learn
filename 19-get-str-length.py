#-*- coding:utf-8 -*-
from tkinter import *
from tkinter import messagebox



def get_Tk():
    top = Tk()
    return top

#定义获取字符长度函数
def sum_test(baseNum):

    return len(baseNum)


def show_result(top,re_sum):
    #这里使用Toplevel(top) 是为了新开一个窗口 ，且显示计算结果，如果直接实例化一个窗口，则新窗口不显示结算结果。
    top_show = Toplevel(top)
    top_show.title("字符长度显示")
    top_show.geometry('300x240+810+420')


    # 显示长度
    Sums = Label(top_show, text='字符长度：')
    Sums.pack()
    sum_text = StringVar()
    sums = Entry(top_show, textvariable=sum_text,state='readonly')
    sum_text.set(re_sum)
    sums.pack()

    top_show.mainloop()

def on_click(top,base_text):

    #获取输入信息
    if base_text.get().strip() == '':
        messagebox.showinfo(title='字符串', message='字符为空，请输入有效的数值！')
    else:
        base_Num = base_text.get()
    strlen = sum_test(base_Num)
    show_result(top,strlen)

def put_info():
    top = get_Tk()
    #top.minsize(100, 100)  # 窗口的最小缩放
    top.title("输入字符串")
    top.geometry('300x240+420+420')


    baseNum = Label(top, text='字符串：')
    baseNum.pack()
    base_text = StringVar()
    base = Entry(top, textvariable=base_text)
    base_text.set(" ")
    base.pack()

    Button(top, text="计算", command= lambda:on_click(top,base_text)).pack()
    top.mainloop()

   # 这种 直接command = 方法名的方式，函数是不能传递参数的，所以为了能传递参数使用了上面的方法。
   # Button(top, text="计算", command= on_click).pack()

if __name__ == '__main__':
    put_info()