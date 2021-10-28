import tkinter as tk

window = tk.Tk()
window.title('my window')

# 窗口尺寸
window.geometry('500x300')
lbl = tk.Label(window, bg='yellow', width=21, text='empty')  # width=21字符的宽度
# lbl = tk.Label(window, bg='yellow', width=20, textvariable=var)  # 第二种写法  不成功
lbl.pack()


def print_selection(v):
    lbl.config(text='you have selected ' + v)  # 第一种写法


s = tk.Scale(window,
             label='try me',
             from_=5,
             to=11,
             orient=tk.HORIZONTAL,
             length=200,
             showvalue=0,
             #variable=var,
             tickinterval=3,
             resolution=0.01,
             command=print_selection
             )  # length=200像素的单位px
s.pack()
# 显示主窗口
window.mainloop()
