from tkinter import *
from tkinter.filedialog import *


#文件选项
def file_open():
    textpad.delete("1.0", END)
    filename = askopenfile(title="选择文件", initialdir="D://daima@//dome//11.15", filetypes=[("文本", ".txt")])
    with open(filename.name,'r') as f:
        content = f.read()
        textpad.insert(INSERT, content)
        global file_name
        file_name = f.name
def file_lingsave():
    files = [('Text Document', '*.txt'), ('All Files', '*.*')]
    file = asksaveasfile(defaultextension='.txt', filetypes=files, initialdir="D://daima@//dome//11.15")
    file.write(textpad.get("1.0", "end"))#读取文本框并且保存地址

def file_quit():
    quit()
#编辑
#帮助
root = Tk()
root.title("记事本")
root.geometry("500x500+200+300")

mn = Menu(root)

mn_f = Menu(mn)
mn_e = Menu(mn)
mn_h = Menu(mn)

mn.add_cascade(label="文件", menu=mn_f)
mn.add_cascade(label="编辑", menu=mn_e)
mn.add_cascade(label="帮助", menu=mn_h)

mn_f.add_command(label="打开", accelerator="ctrl+n", command=file_open)
mn_f.add_command(label="另存为", accelerator="ctrl+s", command=file_lingsave)
mn_f.add_command(label="退出", accelerator="ctrl+n", command=file_quit)
root["menu"] = mn

textpad = Text(root, width=500, height=500)
textpad.pack()

root.mainloop()