import tkinter.filedialog
from tkinter import *
def func1():
    a=tkinter.filedialog.asksaveasfilename()#返回文件名
    print(a)
    a =tkinter.filedialog.asksaveasfile()#会创建文件
    print(a)
    a =tkinter.filedialog.askopenfilename()#返回文件名
    print(a)
    a =tkinter.filedialog.askopenfile()#返回文件流对象
    print(a)
    a =tkinter.filedialog.askdirectory()#返回目录名
    print(a)
    a =tkinter.filedialog.askopenfilenames()#可以返回多个文件名
    print(a)
    a =tkinter.filedialog.askopenfiles()#多个文件流对象
    print(a)
root=Tk()
btn1=Button(root,text="click",command=func1)
btn1.pack()
root.mainloop()
