from tkinter import *
from tkinter.filedialog import *

def text1():
    filename = askopenfile(title="选择文件", initialdir="d:", filetypes=[("文本", "text")])
    print(filename.name)

#
def text1():
    filename = asksaveasfile(title="选择文件", initialdir="d:", filetypes=[("文本", "text")])
    print(filename.name)


root = Tk()
root.title("打开文件")
root.geometry("500x500+200+300")

Button(root,text="选择文件", command=text1).pack()

root.mainloop()
