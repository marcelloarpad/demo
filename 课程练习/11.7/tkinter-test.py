from tkinter import *
from tkinter import messagebox

root=Tk()

root.title("我的第一个GUI程序")
root.geometry("500x300-200-300")

btn01=Button(root)
btn01["text"]="点击送优惠卷"
btn01.pack()

def songquan(e):
    messagebox.showinfo("消息","送你一万块优惠劵")

btn01.bind("<Button-1>",songquan)

root.mainloop()