"""这是一个非常简单的游戏。这里有 21 根棍子，首先用户选 1 到 4 根棍子，然后电脑选 1
到 4 根棍子。谁选到最后一根棍子谁就输。判断一下用户有赢的机会吗？如果没有的话，如何修
改游戏规则可以使用户有赢的机会呢？
特别说明：用户和电脑一次选的棍子总数只能是 5。"""

#!/usr/bin/env python3
sticks = 22

print("每次拿1-4根棍子")
print("谁拿到最后一根棍子就输")

while True:
    print("Sticks left: ", sticks)
    if sticks == 1:
        print("You took the last stick, you lose")
        break
    sticks_taken = int(input("Take sticks(1-4):"))
    if sticks_taken >= 5 or sticks_taken <= 0:
        print("Wrong choice")
        continue
    if sticks >=4:
        computer_taken = 5 - sticks_taken
        print("电脑选择：{}".format(computer_taken))
        sticks -= 5
    else:
        print("你赢了")
    if sticks > 0:
        continue
    elif sticks < 0 or sticks == 1:
        print("你赢了")
        break

