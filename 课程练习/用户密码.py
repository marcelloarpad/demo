doc1 = {}
doc2 = {}
def zhang_hu():
    a = input("定义用户名：")
    b = input("定义密码：")
    doc1[a] = b

def xiu_gai():
    a = input("定义用户名：")
    b = input("定义密码：")
    doc2[a] = b
    if doc1 == doc2:
        print("登陆成功,请修改密码。")
        doc1[a] = input("请输入新密码：")
    else:
        print("登录失败！！！")

def denlu():
    c = 1
    while c<=3:
        a = input("请输入你的账号：")
        b = input("请输入密码：")
        doc2[a] = b
        if doc1 == doc2:
            print("登陆成功！！！")
            break
        else:
            print(f"输入错误，你还剩于{3-c}次机会。")
        c +=1

def main():
    print("1、注册账号\n2、登录账号\n3、修改密码")
    uern = input("请输入选项")
    if uern=="1":
        zhang_hu()
    elif uern=="2":
        denlu()
    elif uern=="3":
        xiu_gai()
    else:
        print("输入错误，请重输")

while True:
    main()