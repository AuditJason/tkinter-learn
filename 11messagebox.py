import tkinter as tk
from tkinter import messagebox
window = tk.Tk()
window.title('my window')

# 窗口尺寸
window.geometry('500x300')


def hit_me():
    # messagebox.showinfo(title='Hi', message='HaHa')
    # messagebox.showerror(title='Hi', message='error')
    # messagebox.showwarning(title='Hi', message='waring')
    print(messagebox.askyesno(title='Hi', message='HaHa'))  # 有返回值的弹窗
tk.Button(window, text='hit me', command=hit_me).pack()


# 显示主窗口
window.mainloop()
