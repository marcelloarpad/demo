from tkinter import *
root=Tk()
root.title("记事本")
root.geometry("500x300+200+309")

v=StringVar()
v.set("M")
r1=Radiobutton(root,text="男",value="M",variable=v)
r2=Radiobutton(root,text="女",value="F",variable=v)
r1.pack(side="left")
r2.pack(side="left")

def confirm():
    sex=v.get()
    if(sex=="M"):
        print("性别是: 男")
    else:
        print("性别是: 女")

Button(root,text="确定",command=confirm).pack(side="left")

root.mainloop()
