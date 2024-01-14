import time
now = time.time()
print(now)

#localtime模块将时间戳转化格式
print("当前时间", time.localtime())

#gmtime转化为0时区
print(time.gmtime())

#asctime
t = (2023, 10, 28, 12, 49, 1, 5, 301, 0)
print(time.asctime(t))

#ctime mk
print(time.ctime())
print(time.ctime(0))

time1 = (2001, 12, 15, 12, 0, 0, 0, 1, 0)
beust = time.mktime(time1)
th = beust-now
