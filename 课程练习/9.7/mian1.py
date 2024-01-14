import os,time
file = os.listdir("D:\\daima@\\dome\\9.7")
cev_time = os.path.getctime("text.jpg") #查找文件创建时间戳
local_time = time.localtime(cev_time) #解析时间戳
formatted_time = time.strftime('%Y_%m_%d-%H：%M：%S',time.localtime(cev_time))#设置时间格式
old_name = "text.jpg"#文件原属名
new_name = f"text {formatted_time}.jpg"#修改后的文件名，加上创建时间
os.rename(old_name, new_name)#替换文件名