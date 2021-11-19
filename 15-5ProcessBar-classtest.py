import time
import tkinter as tk
import tkinter.ttk


class CreateStatus:
    def __init__(self, master, fontsize, side='left'):
        # 状态栏
        self.status = tk.StringVar()
        self.status.set('状态栏')
        tk.Label(
            master,
            textvariable=self.status,
            font=fontsize  # ,
            ).pack(side=side)


class CreateProcessBar:
    def __init__(self, master, maxbyte: int):
        self.new_window = tk.Toplevel(master)
        self.new_window.title('程序进度')
        winWidth, winHeight, x, y = 550, 60, 300, 300
        self.new_window.geometry("%sx%s+%s+%s" % (winWidth, winHeight, x, y))
        self.progressbarOne = tkinter.ttk.Progressbar(self.new_window, length=548)
        self.progressbarOne.pack(pady=10)
        self.progressbarOne['value'] = 1
        self.progressbarOne['maximum'] = maxbyte
        self.status =CreateStatus(self.new_window, 10, )
        self.status.status.set('程序处理进度......')

    def show(self, byte, text):
        self.progressbarOne['value'] = byte
        self.status.status.set('正在处理: {}'.format(text))
        self.new_window.update()



root = tk.Tk()
root.geometry('550x220')
def theshow():
    maxtype = 100
    psg = CreateProcessBar(root, maxtype)
    for n in range(0, maxtype+1, 10):
        psg.show(n, str(n))
        time.sleep(0.1)

button = tk.Button(root, text='Running', command=theshow)
button.pack(pady=5)
root.mainloop()
