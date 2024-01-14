from tkinter import *
from tkinter.colorchooser import *

def text1():
    c1 = askcolor(color="red", title="背景色")
    root.config(background = c1[1])

root = Tk()
root.title("颜色选择")
root.geometry("500x500+200+100")

Button(root,text="颜色选择", command=text1).pack()
root.mainloop()