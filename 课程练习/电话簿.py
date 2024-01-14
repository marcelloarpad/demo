dic ={}
#添加通讯录用户
def tian_jia ():
    a = input("请输入用户名字：")
    b = input("请输入电话号码:")
    return a, b
#显示所有用户姓名
def daying ():
    print(dic)

def main():
    print("1.添加联系人 \n2.显示所有联系人")
    uern = input("请输入你的选项:")
    if uern == "1":
        tian_jia()
    elif uern == "2":
        daying()

while True:
    main()