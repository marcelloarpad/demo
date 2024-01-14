from tkinter import *

root=Tk()
root.title("Label演示")
root.geometry("500x300+200+300")

label01=Label(text="政南吃瓜",width=10,height=2,bg="pink",fg="blue",font=("幼圆",30))
label01.pack()

root.mainloop()