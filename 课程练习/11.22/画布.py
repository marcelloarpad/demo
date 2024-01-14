from tkinter import *
from tkinter.colorchooser import askcolor
#主窗体高
win_hight = 450
win_width = 800

#初始化背景色
bgcolor = "#000000"
fgcolor = "#ffffff"

x = 0
y = 0
lastDraw = 0
starDrawflag = False

def eventManage(event):
    name = event.widget.winfo_name()
    print(name)
    if name == "pen":
        drawpad.bind("<B1-Motion>", mypen)
    elif name == "rect":
        drawpad.bind("<B1-Motion>", myrect)
    elif name == "oval":
        drawpad.bind("<B1-Motion>", myyuan)
    elif name == "clean":
        drawpad.delete("all")
    elif name == "erasor":
        drawpad.bind("<B1-Motion>", myerasor)
    elif name == "line":
        drawpad.bind("<B1-Motion>", myline)
    elif name == "arrow":
        drawpad.bind("<B1-Motion>", myarrow)
    elif name == "pen_color":
        global fgcolor
        pen_color = askcolor(color=fgcolor, title="选择画笔颜色")
        fgcolor = pen_color[1]
    elif name == "bg_color":
        global bgcolor
        bgcolor = askcolor(color=bgcolor, title="选择画笔颜色")[1]
        drawpad.config(bg = bgcolor)

def mypen(event):#自由画笔
    global lastDraw, x, y, starDrawflag
    if not starDrawflag:
        starDrawflag = True
        x = event.x
        y = event.y
    lastDraw = drawpad.create_line(x, y, event.x, event.y, fill=fgcolor)
    x = event.x
    y = event.y

def myrect(event):#矩形
    global lastDraw, x, y, starDrawflag
    drawpad.delete(lastDraw)
    if not starDrawflag:
        starDrawflag = True
        x = event.x
        y = event.y
    lastDraw = drawpad.create_rectangle(x, y, event.x, event.y, outline=fgcolor)

def myyuan(event):#圆形
    global lastDraw, x, y, starDrawflag
    drawpad.delete(lastDraw)
    if not starDrawflag:
        starDrawflag = True
        x = event.x
        y = event.y
    lastDraw = drawpad.create_oval(x, y, event.x, event.y, outline=fgcolor)

def myerasor(event):
    global lastDraw, x, y, starDrawflag
    if not starDrawflag:
        starDrawflag = True
        x = event.x
        y = event.y
    lastDraw = drawpad.create_line(x, y, event.x, event.y, fill=bgcolor, width=10)
    x = event.x
    y = event.y

def myline(event):#直线
    global lastDraw, x, y, starDrawflag
    drawpad.delete(lastDraw)
    if not starDrawflag:
        starDrawflag = True
        x = event.x
        y = event.y
    lastDraw = drawpad.create_line(x, y, event.x, event.y, fill=fgcolor)

def myarrow(event):
    global lastDraw, x, y, starDrawflag
    drawpad.delete(lastDraw)
    if not starDrawflag:
        starDrawflag = True
        x = event.x
        y = event.y
    lastDraw = drawpad.create_line(x, y, event.x, event.y, arrow=LAST, fill=fgcolor)

def starDraw(event):
    global lastDraw, x, y, starDrawflag
    starDrawflag = False
    lastDraw = 0

root = Tk()
root.title("画图")
root.geometry(f"{str(win_width)}x{str(win_hight)}+200+300")

drawpad = Canvas(root, width=win_width,height=win_hight*0.9,bg=bgcolor)
drawpad.pack()

#初始化开始菜单
"""mun = Menu(root)
mun_s = Menu(mun)
mun.add_cascade(label="文件", menu=mun_s)
def file_open():
    pass
def file_lingsave():
    pass
def file_quit():
    pass

mun_s.add_command(label="打开", accelerator="ctrl+n", command=file_open)
mun_s.add_command(label="另存为", accelerator="ctrl+s", command=file_lingsave)
mun_s.add_command(label="退出", accelerator="ctrl+n", command=file_quit)
root["menu"] = mun"""

bnt_pen = Button(root, text="画笔", name="pen")
bnt_pen.pack(side="left", padx="10")
bnt_rect = Button(root, text="矩形", name="rect")
bnt_rect.pack(side="left", padx="10")
bnt_oval = Button(root, text="圆形", name="oval")
bnt_oval.pack(side="left", padx="10")
bnt_clean = Button(root, text="清屏", name="clean")
bnt_clean.pack(side="left", padx="10")
bnt_erasor = Button(root, text="橡皮擦", name="erasor")
bnt_erasor.pack(side="left", padx="10")
bnt_line = Button(root, text="直线", name="line")
bnt_line.pack(side="left", padx="10")
bnt_arrow = Button(root, text="箭头直线", name="arrow")
bnt_arrow.pack(side="left", padx="10")
bnt_canv_color = Button(root, text="画布颜色", name="bg_color")
bnt_canv_color.pack(side="left", padx="10")
bnt_pen_color = Button(root, text="画笔颜色", name="pen_color")
bnt_pen_color.pack(side="left", padx="10")

bnt_line.bind_class("Button", "<1>", eventManage)
drawpad.bind("<ButtonRelease-1>", starDraw)
root.mainloop()