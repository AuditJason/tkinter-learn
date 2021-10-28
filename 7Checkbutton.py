# 教程地址：
# https://mofanpy.com/tutorials/python-basic/tkinter/checkbutton/
import tkinter as tk

window = tk.Tk()
window.title('my window')

# 窗口尺寸
window.geometry('500x300')

lb = tk.Label(window, bg='yellow', width=21, text='empty')  # width=21字符的宽度
lb.pack()


def print_selection():
    if (var1.get() == 1) & (var2.get() == 0):  # 如果选中第一个选项，未选中第二个选项
        lb.config(text='I love only Python ')
    elif (var1.get() == 0) & (var2.get() == 1):  # 如果选中第二个选项，未选中第一个选项
        lb.config(text='I love only C++')
    elif (var1.get() == 0) & (var2.get() == 0):  # 如果两个选项都未选中
        lb.config(text='I do not love either')
    else:
        lb.config(text='I love both')  # 如果两个选项都选中


var1 = tk.IntVar()
var2 = tk.IntVar()
c1 = tk.Checkbutton(window,
                    text='Python',
                    variable=var1,
                    onvalue=1,
                    offvalue=0,
                    command=print_selection)
c2 = tk.Checkbutton(window, text='C++', variable=var2, onvalue=1, offvalue=0,
                    command=print_selection)
c1.pack()
c2.pack()
# 显示主窗口
window.mainloop()
