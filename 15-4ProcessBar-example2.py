import time
import tkinter
import tkinter.ttk


def show():
    while progressbarOne.cget('value') <= progressbarOne['maximum']:
        progressbarOne.step(2)
        root.update()
        print(progressbarOne.cget('value'))
        time.sleep(0.05)


root = tkinter.Tk()
root.geometry('350x220')

progressbarOne = tkinter.ttk.Progressbar(root, length=200, mode='determinate', orient=tkinter.HORIZONTAL)
progressbarOne.pack(pady=20)

progressbarOne['maximum'] = 100
progressbarOne['value'] = 0


button = tkinter.Button(root, text='Running', command=show)
button.pack(pady=5)

root.mainloop()
