class Student(object):  # object 为继承的对象

    course = 'ML'  # 类变量的定义

    def __init__(self, name, age):  # 类似于java中的构造函数，这个是对象创建的时候必须绑定的变量
        self.name = name
        self.age = age
        self.__score = 10  # 所有__开头的变量都是私有变量

    def print_info(self):
        print("name %s:%s" % (self.name, self.age))  # 格式化打印

    def __len__(self):
        return 5


# python 中也有继承和多态，但是没有java中那么严格，比较相像的对象都可以使用多态的特性

import sys
if __name__=='__main__':#直接运行时，python会把__name__赋值为__main__
    s = Student('liu', '10')
    s.sex = '男'
    print('类变量:%s ，直接读取类变量:%s' % (s.course, Student.course))
    s.print_info()
    print(s.sex)
    print(len(s))  # 多态调用示例
    print(sys.argv)#打印传入的变量

