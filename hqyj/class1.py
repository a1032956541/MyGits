class Student:
    '''
    学生类
    '''
    #数据成员
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex
    #行为成员，成员方法，成员函数
    def study(self):
        print(f"{self.name}正在学习")
    def introduce(self):
        print(f'大家好，我是{self.name},今年{self.age}岁了。')


zf = Student('张飞',18,"男")#调用的是Student 类中__init__函数
zf.introduce()
gy = Student('关羽',20,'男')
gy.study()