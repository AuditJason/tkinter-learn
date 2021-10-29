import tkinter
import tkinter.ttk
root = tkinter.Tk()
root.geometry('150x120')

progressbarOne = tkinter.ttk.Progressbar(root)
progressbarOne.pack(pady=20)
# 进度值最大值
progressbarOne['maximum'] = 100
# 进度值初始值
progressbarOne['value'] = 20
# 横排 长度200 起点移至终点
progressbarTwo = tkinter.ttk.Progressbar(root, orient=tkinter.HORIZONTAL, length=200, mode='determinate')
progressbarTwo.pack(pady=20)
# 进度值最大值
progressbarTwo['maximum'] = 100
# 进度值初始值
progressbarTwo['value'] = 80
# 注意：现在进度条还不能动！
root.mainloop()
