import tkinter as tk

window = tk.Tk()
window.title('my window')

# 窗口尺寸
window.geometry('500x300')

# pack直接放置
tk.Label(window, text=1).pack(side='top')
tk.Label(window, text=1).pack(side='bottom')
tk.Label(window, text=1).pack(side='left')
tk.Label(window, text=1).pack(side='right')


# 显示主窗口
window.mainloop()
