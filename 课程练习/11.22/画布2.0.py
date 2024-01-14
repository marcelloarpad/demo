from tkinter import *
from tkinter.colorchooser import askcolor



class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.createWidget()
        self.x = 0
        self.y = 0
        self.lastDraw = 0  # 最后绘制的图形id
        self.startDrawFlag = False
        self.color = "red"
        self.beijingcolor = "black"


    def createWidget(self):
        # 创建绘图区
        self.drawPad = Canvas(root, width=900, height=500, bg="black")
        self.drawPad.pack()

        # 画图软件的各种按钮
        btn_pen = Button(self, text="画笔", name="pen")
        btn_pen.pack(side="left", padx="10")
        btn_rect = Button(self, text="矩形", name="rect")
        btn_rect.pack(side="left", padx="10")
        btn_yuan = Button(self, text="圆形", name="yuan")
        btn_yuan.pack(side="left", padx="10")
        btn_clear = Button(self, text="清屏", name="clear")
        btn_clear.pack(side="left", padx="10")
        btn_erasor = Button(self, text="橡皮擦", name="erasor")
        btn_erasor.pack(side="left", padx="10")
        btn_line = Button(self, text="直线", name="line")
        btn_line.pack(side="left", padx="10")
        btn_lineArrow = Button(self, text="箭头直线", name="lineArrow")
        btn_lineArrow.pack(side="left", padx="10")
        btn_color = Button(self, text="颜色", name="pen_color")
        btn_color.pack(side="left", padx="10")
        btn_bj = Button(self, text="背景", name="beijing")
        btn_bj.pack(side="left", padx="10")
        # 为所有button绑定事件
        btn_pen.bind_class("Button", "<1>", self.eventManage)
        self.drawPad.bind("<ButtonRelease-1>", self.stopDraw)

    def stopDraw(self, event):
        self.startDrawFlag = False
        self.lastDraw = 0

    def startDraw(self, event):
        self.drawPad.delete(self.lastDraw)
        if not self.startDrawFlag:
            self.startDrawFlag = True
            self.x = event.x
            self.y = event.y

    def eventManage(self, event):
        name = event.widget.winfo_name()
        print(name)
        if name == "line":
            self.drawPad.bind("<B1-Motion>", self.myline)
        elif name == "lineArrow":
            self.drawPad.bind("<B1-Motion>", self.mylineArrow)
        elif name == "rect":
            self.drawPad.bind("<B1-Motion>", self.myRect)
        elif name == "yuan":
            self.drawPad.bind("<B1-Motion>", self.myyuan)
        elif name == "pen":
            self.drawPad.bind("<B1-Motion>", self.myPen)
        elif name == "erasor":
            self.drawPad.bind("<B1-Motion>", self.myErasor)
        elif name == "clear":
            self.drawPad.delete("all")
        elif name == "pen_color":
            c1 = askcolor(color=self.color, title="选择画笔颜色")
            self.color = c1[1]
            print(self.color)
        elif name == "beijing":
            c2 = askcolor(color=self.beijingcolor, title="更改画布颜色")
            self.beijingcolor = c2[1]
            print(self.beijingcolor)





    def myline(self, event):
        self.startDraw(event)
        self.lastDraw = self.drawPad.create_line(self.x, self.y, event.x, event.y, fill=self.color)

    def mylineArrow(self, event):
        self.startDraw(event)
        self.lastDraw = self.drawPad.create_line(self.x, self.y, event.x, event.y, arrow=LAST, fill=self.color)

    def myRect(self, event):
        self.startDraw(event)
        self.lastDraw = self.drawPad.create_rectangle(self.x, self.y, event.x, event.y, outline=self.color)
    def myyuan(self, event):
        self.startDraw(event)
        self.lastDraw = self.drawPad.create_oval(self.x, self.y, event.x, event.y, outline=self.color)
    def myPen(self, event):
        self.startDraw(event)
        self.drawPad.create_line(self.x, self.y, event.x, event.y, fill=self.color)
        self.x = event.x
        self.y = event.y

    def myErasor(self, event):
        self.startDraw(event)
        self.drawPad.create_rectangle(event.x - 3, event.y - 3, event.x + 3, event.y + 3, fill="black")
        self.x = event.x
        self.y = event.y


if __name__ == '__main__':
    root = Tk()
    root.geometry("900x500+200+200")
    root.title("画图软件")
    app = Application(master=root)
    root.mainloop()
