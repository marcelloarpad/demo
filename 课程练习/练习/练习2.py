'''问题:编写一个可以计算给定数的阶乘的程序。结果应该以逗号分隔的顺序打印在一行上。假设向程序提供以下输入:8
则输出为:40320
提示:在为问题提供输入数据的情况下，应该假设它是控制台输入。
解决方案:'''

'''def fact(x):
    if x==0:
        print("阶乘为1")
    return x * fact(x - 1)
a = input("请输入一个数字")
fact(a)'''

def fact(x):
    if x == 0:
        return 1
    return x * fact(x - 1)
print('请输入一个数字：')
x=int(input())
print (fact(x))
