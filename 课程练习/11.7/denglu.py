import tkinter
from tkinter import *

root=Tk()
root.title("登录")
root.geometry("500x300+200+300")

label01 = Label(root, text="账号:").pack()
label02 = Label(root, text="密码：").pack()

e1 = tkinter.Entry(root)
e2 = tkinter.Entry(root, show='*')

e1.grid


"""label01=Label(text="政南吃瓜",width=10,height=2,bg="pink",fg="blue",font=("幼圆",30))
label01.pack()"""









root.mainloop()