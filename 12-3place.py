import tkinter as tk

window = tk.Tk()
window.title('my window')

# 窗口尺寸
window.geometry('500x300')

# place直接放置

tk.Label(window, text='label').place(x=10, y=100, anchor='nw')


# 显示主窗口
window.mainloop()
