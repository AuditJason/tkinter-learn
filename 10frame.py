# https://mofanpy.com/tutorials/python-basic/tkinter/frame/
import tkinter as tk

window = tk.Tk()
window.title('my window')

# 窗口尺寸
window.geometry('500x300')

tk.Label(window,  text='om the window').pack()  # width=21字符的宽度

frm = tk.Frame(window,)
frm.pack()
frm_l = tk.Frame(frm,)

frm_r = tk.Frame(frm,)
frm_l.pack(side='left')
frm_r.pack(side='right')

tk.Label(frm_l, text='on the frm_l1').pack()
tk.Label(frm_l, text='on the frm_l2').pack()
tk.Label(frm_r, text='on the frm_r').pack()

# 显示主窗口
window.mainloop()
