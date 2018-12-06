
import math
print(math)
print(math.ceil(5.04))  # 向上取整
print(math.floor(5.04))  # 向下取整
print("="*20)

import keyword
print(keyword.kwlist)
print(round(5.1315))  # 四舍五入
print(math.sqrt(9))  # 平方根
print(math.pow(2,3))  # 幂运算，返回浮点数
print(2**3)  # 幂运算，返回整数
print("="*20)
print(math.fabs(-3))  # 绝对值，返回浮点数
print(abs(-3.5))  # python内置函数，可返回相应类型的数值
print("="*20)
print(math.fsum([1,2,3,4,5]))  # math模块的求和，返回浮点数
print(sum([1,2,3,4,5]))  # 内置求和函数
print("="*20)
print(math.modf(18.25))  # 将浮点数拆分成小数和整数
print(math.copysign(2,-3))  # 复制y的符合给x,返回浮点数
print("="*20)
print(math.e)  # 自然对数
print(math.pi)  # 圆周率π

###########################
print("="*20)
import random
for i in range(10):
    print(random.random())  # random() 获取0-1之间的随机小数，左闭右开区间
for i in range(10):
    print(random.randrange(1,20))  # randrange() 获取随机整数，左闭右开区间
print("="*20)
for i in range(5):
    print(random.randint(1,20))
print("="*20)
list1=[1,4,67,89,34,35]
print(random.choice(list1))  # 随机获取列表中的值，choices多个值，list,tuple
random.shuffle(list1)  # 打乱列表顺序
print(list1)

print("="*20)
import random
for i in range(3):
    print(random.uniform(1,10))  # 随机获取指定范围内的值，包括小数