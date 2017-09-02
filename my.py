#!/usr/bin/env python3
# -*- coding: utf-8 -*-
d = "d"
print(d)
print(1 - 2)

print("hello", "world")

# name = input()  # 接受控制台输入
# print("hello", name)

str = '''test
    test
'''
print(str)

# 大小写敏感,惯例使用全大写标识常量
Name = "up"
name = "low"
print(Name, name)

# python对整数没有大小限制


# python 中变量引用和java中有很大区别,python每次都会对新的变量值申请新的内存空间
a = 1
b = a
a = a + 2
print(a, b)  # 结果为 3 1

"中文".encode("utf-8")
print(len("中文"))

## list 和tuple 定义方式不一样,tuple定义了后不能进行更改,访问方式是一样的
li = ["a", 'b', 2]
print(li)
tuple_1 = ('a', 2)
print(len(li), len(tuple_1))
li.insert(3, 'd')
li.append('e')
tuple_2 = (2,)  # 定义两个长度的tupel
tuple_2 = (1, 'b')
print(tuple_2, tuple_2[0])
print(li, li[2])
for i, value in enumerate(li):
    print("index->value", i, value)

# map set 对应dic
dic = {'a': 1, 'b': b}
print(dic['a'], 'a' in dic)  # dic[a]如果a对应的值不存在会报错
print(dic.get('bc', -1), dic.get('bda'))  # 也可以通过get方式获取
if dic.get('bcd') == None:
    print('dic中没有的值返回None,等同于java中的null')
set = ([1, 2, 3])  # set定义规范
print(set)

for m in dic:
    print("key=", m)
for m in dic.items():
    print("key+value=", m[0], m[1])

# python 使用缩进来判断是否是代码快,与java中的{}功能类似
age = 10
if age == 10:
    print(age)
    print('goods')
else:
    print('1')
print('d')

# 条件判断和循环都是:后面接代码快
for x in range(5):
    print(x)
x = 1
while x < 3:
    print(x)
    x = x + 1

# python函数参数顺序
# 必选参数 只有参数名
# 默认参数  参数名=值
# 可变参数  *参数名
# 命名关键字参数 *,参数名
# 关键字参数 **参数名

# 参数使用
# *arg 是可变参数,args是一个tuple  类似与java中的数据参数
# **kw 是关键字参数,kw是一个dict     类似与java中的map参数

# 函数的参数尽量使用不可变对象


# 字符串的截取操作,可以使用list tuple的slice操作
print('abc'[0:2])  # 输出ab

# 列表生成器 generate
# 只要把一个列表生成式的[]改成()，就创建了一个generator
# generate 类似算法的快照,只在调用next(g)时,才计算值,不会像生成器那样占用内存,函数中使用yield 语句后,函数也会变成generate函数
l = [x for x in range(10)]
g = (x for x in range(10))

# 返回函数中,不要引用可能变化的变量.
# 匿名函数需要使用关键字lamdba

print(list(map(lambda x: x * 2, [1, 2, 3])))

# 偏函数，相当于对java中的函数进行重构,需要使用 functools.partial
import functools

int2 = functools.partial(int, base=10)
print(int2('123'))
print(int.__name__)  # 获取函数的名称

# python中代表每个package中需要有标记文件__init__.py，来说明是个包文件
import alan.test.Student as st

s=st.Student('liu','10')
s.sex='男'
s.print_info()
print(s.sex)
print(len(s))
