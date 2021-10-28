import tkinter as tk

window = tk.Tk()
window.title('my window')

# 窗口尺寸
window.geometry('500x300')


def insert_point():
    var = e.get()
    t.insert('insert', var)


def insert_end():
    var = e.get()  # 获取e的输入值
    t.insert('end', var)  # 将获取到的e的输入值传给t


e = tk.Entry(window, show='*')
e.pack()

b1 = tk.Button(window,
               text="insert point",
               width=15,
               height=2,
               command=insert_point)
b1.pack()

b2 = tk.Button(window, text="insert end", command=insert_end)
b2.pack()

t = tk.Text(window, height=2)
t.pack()

# 显示出来
window.mainloop()
