num = int(input("请输入需要判断的3位数："))
num1 = (num%100)%10
num10 = (num%100)//10
num100 = num//100
if num1**3+num10**3+num100**3 ==num:
    print(f"{num}是水仙花数")
else:
    print(f"{num}不是水仙花数")