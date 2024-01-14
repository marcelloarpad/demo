class Dog:
    role = "dog"

    def __init__(self, name, breed, attack_val):
        self.name = name   #狗的名字
        self. breed = breed   #狗的品种
        self. attack_val = attack_val  #狗的伤害
        self.life_val = 100#初始血量

    def bite(self, person):#传递person这个对象
        person.life_val -= self.attack_val
        print(f"狗{self.name}咬了人{person.neme}，人掉血{self.attack_val},还剩血量{person.life_val}..")

class Person:
    rale = "person"

    def __init__(self,name, sex, attack_val):
        self.name = name
        self.sex = sex
        self.attack_val = attack_val
        self.life_val = 100

    def attack(self, dog):
        dog.life_val -= self.attack_val
        print("人[%s]打了狗[%s],狗掉血[%s],还剩血量[%s].." %(self.name, dog.name, self.attack_val, dog.attack_val))

d = Dog("mjj", "二哈",30)

p = Person("张三", "男", 45)

p.attack(d)
d.bite(p)
