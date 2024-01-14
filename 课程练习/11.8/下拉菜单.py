from tkinter import *
from tkinter import messagebox

root=Tk()
root.title("记事本")
root.geometry("500x300+200+300")

school=StringVar()
school.set("云南民族大学")
om=OptionMenu(root,school,"西南林业大学","云南农业大学","云南民族大学","大理大学","师范学院")
om["width"]=10
om.pack()

def confirm():
    print("报考的学校是:",school.get())

Button(root,text="确认",command=confirm).pack()

root.mainloop()