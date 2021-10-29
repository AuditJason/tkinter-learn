import time
import tkinter
import tkinter.ttk


def show():
    for i in range(100):
        progressbarOne['value'] = i+1
        # 更新画面
        root.update()
        time.sleep(0.5)


root = tkinter.Tk()
root.geometry('350x220')

progressbarOne = tkinter.ttk.Progressbar(root)
progressbarOne.pack(pady=20)
# 进度值最大值
progressbarOne['maximum'] = 100
# 进度值初始值
progressbarOne['value'] = 0
# 横排 长度200 起点移至终点

button = tkinter.Button(root, text='runing', command=show)
button.pack(pady=5)

root.mainloop()
