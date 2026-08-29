class Student:
    school = "清华"

    def __init__(self, name):
        self.name = name


a = Student("张三")
b = Student("李四")
a.school = "北大"
print(b.school)
print(a.school)