from tkinter import *

root = Tk()
root.title("记事本")
root.geometry("500x300+200+300")

w1=Text(root,width=60,height=18,bg="gray")
w1.pack()
w1.insert(1.0,"adsfasf\nfddafa")
w1.insert(4.0,"昆明治金高等专科学校")

def insertText():
    w1.insert(INSERT,"kmyz")
    w1.insert(END,"net2235")
def returnText():
    print(w1.get(1.2,1.6))
    print("所有文本: n",w1.get(1.9,END))

Button(text="重复插入文本",command=insertText).pack(side="left")
Button(text="返回文本",command=returnText).pack(side="left")

root.mainloop()