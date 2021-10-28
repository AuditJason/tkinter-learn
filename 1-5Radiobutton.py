import tkinter as tk

window = tk.Tk()
window.title('my window')

# 窗口尺寸
window.geometry('500x300')

var = tk.StringVar()
lbl = tk.Label(window, bg='yellow', width=21, text='empty')  # 第一种写法
# lbl = tk.Label(window, bg='yellow', width=20, textvariable=var)  # 第二种写法  不成功
lbl.pack()


def print_selection():
    lbl.config(text='you have selected ' + var.get())  # 第一种写法
    # var.set('you have selected {}'.format(var.get()))  # 第二种写法  不成功


var.set(0)  # 默认选择按钮全没选中
r1 = tk.Radiobutton(window,
                    text='Option A',
                    variable=var,
                    value='A',
                    command=print_selection)
r1.pack()

r2 = tk.Radiobutton(window,
                    text='Option B',
                    variable=var,
                    value='B',
                    command=print_selection)
r2.pack()

r3 = tk.Radiobutton(window,
                    text='Option C',
                    variable=var,
                    value='C',
                    command=print_selection)
r3.pack()
# 显示主窗口
window.mainloop()
