from tkinter import *
from tkinter import messagebox
root = Tk()

def comfirm():
    if videoHobby.get() == 1:
        messagebox.showinfo("测试","看视频，是正常人有的爱好!")
    if codeHobby.get() == 1:
        messagebox.showinfo("测试","抓获野生程序猿一只.")

codeHobby = IntVar()
videoHobby = IntVar()
print(codeHobby.get())# 默认值是
c1=Checkbutton(root,text="敲代码",variable=codeHobby,onvalue=1,offvalue=8)
c2=Checkbutton(root,text="看视频",variable=videoHobby,onvalue=1,offvalue=8)
c1.pack(side="left")
c2.pack(side="left")
Button(root,text="确定",command=comfirm).pack(side="left")

root.mainloop()