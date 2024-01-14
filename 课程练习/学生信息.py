class StudentsSter:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.grades = {"语文": 0, "数学": 0, "英语": 0}

    def set_graden(self, course, grade):
        if course in self.grades:
            self.grades[course] = grade
    def print_drade(self):
        print(f"学生{self.name}(学号{self.id}) 的成绩:")
        for course in self.grades:
            print(f"{course}: {self.grades[course]}分")
chen = StudentsSter("小陈", "1035")
chen.print_drade()




