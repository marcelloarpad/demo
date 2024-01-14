wage = float(input("请输入你的工资："))
if  0 < wage <= 5000:
    print("税率为0%，个人所得税为0")
elif 5000 < wage <= 8000:
    tex_money = wage*0.03
    print(f"税率为3%，个人所得税为{tex_money}")
elif 8000 < wage <= 17000:
    tex_money = wage*0.1
    print(f"税率为10%，个人所得税为{tex_money}")
elif 1700 < wage <= 30000:
    tex_money = wage*0.2
    print(f"税率为20%，个人所得税为{tex_money}")
elif 30000 < wage <= 40000:
    tex_money = wage*0.25
    print(f"税率为25%，个人所得税为{tex_money}")
elif 40000 < wage <= 60000:
    tex_money = wage*0.3
    print(f"税率为30%，个人所得税为{tex_money}")
elif 60000 < wage <= 85000:
    tex_money = wage*0.35
    print(f"税率为35%，个人所得税为{tex_money}")
elif wage > 85000:
    tex_money = wage*0.45
    print(f"税率为45%，个人所得税为{tex_money}")
else:
    print("输入错误请重新输入")



