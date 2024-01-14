def func1():
    a = int(input("请输入第一个数："))
    b = int(input("请输入第二个数："))
    a1,b1 = a,b
    t=1
    for i in range(2,min(a,b)):
        while(a % i == 0 and b % i == 0):
            t=t*i
            a=a/i
            b=b/i
    print("%s,%s的最大公约数为：%s" %(a1,b1,t))

if __name__ == '__main__':
    func1()