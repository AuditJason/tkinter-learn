import tkinter as tk

window = tk.Tk()
window.title('my window')

# 窗口尺寸
window.geometry('500x300')

# pack直接放置
for i in range(4):
    for j in range(3):
        tk.Label(window, text='label').grid(row=i, column=j, ipadx=10, ipady=10)


# 显示主窗口
window.mainloop()
