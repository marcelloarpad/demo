list =[2, 4, 5, 5, 5, 44, 3, 5]
print(sorted(list))

shopping_list = []
shopping_list.append("键盘")
shopping_list.append("鼠标")
shopping_list.append("耳机")
shopping_list.append("屏幕")
shopping_list.append("主机")

print(shopping_list)
print(len(shopping_list))
print(shopping_list[1])

shopping_list.remove("鼠标")
print(shopping_list)
print(len(shopping_list))
a = shopping_list[2]
print(a)

shopping_list[1] = "键盘"
print(shopping_list)
price = [22, 44, 55, 22, 44]
print(min(price))
print(max(price))