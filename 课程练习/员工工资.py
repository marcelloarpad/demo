class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def print_info(self):
        print(f"员工姓名：{self.name}, 工号：{self.id}")

class FullTimeEmployee(Employee):
    def __init__(self, name, id, monthly_salary):
        super().__init__(name, id)
        self.monthly_salary = monthly_salary

    def calculate_monthly_pay(self):
        return self.monthly_salary

class PartTimeEmployee(Employee):
    def __init__(self, name, id, daily_salary, work_days):
        super().__init__(name, id)
        self.daily_salary = daily_salary
        self.work_days = work_days

    def calculate_monthly_pay(self):
        return self.work_days*self.daily_salary

zhangshan = FullTimeEmployee("张三", "1035", 6000)
lisi = PartTimeEmployee("李四", "13025", 100, 15)

lisi.print_info()
zhangshan.print_info()

print(lisi.calculate_monthly_pay())
print(zhangshan.calculate_monthly_pay())

