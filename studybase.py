# apple=100
# print(apple)
# print('apple')

# a=5
# b=5.0
# c='5'
# d=True
# print(type(a),type(b),type(c),type(d))

# egg = float(input('请输入一个数字：'))
# print(egg,type(egg))

# print(58%2, 67%2, 58//2, 67//2)

# a=abs(5)
# b=divmod(5,10)
# c=pow(5,10)
# print(a,end='')
# print(b,end='')
# print(c)

# 条件判断
# import random
# i=random.randint(1,50)
# if i > 100:
#     print('超出范围')
# else:
#     print(f'生成的数字是：{i}')

# 循环 计算1-100的奇数和
# sum=0
# for i in range(1,101):
#     if i%2 != 0:
#         sum = sum + i
# print(sum)

# i=0
# sum=0
# while i < 101:
#     if i % 2 != 0:
#        sum = sum + i
#     i = i + 1
# print(sum)

#三位数排列组合
# count = 0
# for i in range(1,5):
#     for j in range(1,5):
#         for k in range(1,5):
#             if i != j and i!= k and j != k:
#                 count = count + 1
#                 print(i,j,k)
# print(count)

#打印乘法口诀表
# for i in range(1, 10):
#     for j in range(1, 1+i):
#         print(f"{i}*{j}={i*j}",end='\t')
#     print(end='\n')

# for i in range(1, 10):
#     for j in range(1, 10):
#         if i >= j:
#             print(f"第{i}列第{j}行",end='\t')
#     print()

# 打印水仙花数
# for i in range(1,10):
#     for j in range(0, 10):
#         for k in range(0, 10):
#             sum_total = i*100+j*10+k
#             if i ** 3 + j ** 3 + k ** 3 == sum_total:
#                 print(sum_total)

# for num in range(100, 1000):
#     i = num // 100
#     j = num // 10 % 10
#     k = num % 10
#     sub_num = i ** 3 + j ** 3 + k ** 3
#     if sub_num == num:
#         print(num)

# 猴子吃桃子
# peaches = 1
# day = 1
# while day <= 9:
#     peaches = (peaches + 1) * 2
#     day += 1
# print(peaches)

# 输入一串字符，数出里面各种字符类型的数量
# s = input("请输入一个字符串：")
# letters = 0
# space = 0
# numbers = 0
# others = 0
# for c in s:
#     if c.isalpha():
#         letters += 1
#     elif c.isdigit():
#         numbers += 1
#     elif c.isspace():
#         space += 1
#     else:
#         others += 1
# print(letters, space, numbers, others)

# 排列元素
# a = [1,5,6,0.5,7,70,8,9.7]
# a.sort(reverse=True)
# print(a)
# b = ['banana','tree','sun']
# b.sort(key=len)
# print(b)
# student = [
# {'sno':101,'sname':'小张','sgrade':88},
# {'sno':102,'sname':'小王','sgrade':77},
# {'sno':103,'sname':'小李','sgrade':98},
# {'sno':104,'sname':'小莫','sgrade':65}
# ]
# sorted_student = sorted(student, key=lambda x:x['sgrade']) #lambda是匿名函数，简化代码
# print(sorted_student)

# 求列表中所有偶数的和
# num = [1,2,3,4,5,6,7,8,9,10]
# num_sum = 0
# for i in num:
#     if i % 2 == 0:
#         num_sum = num_sum + i
# print(num_sum)

# class Solution:
#     def findTheDifference(self, s: str, t: str) -> str:
#         for i in t:
#             if i not in s:
#                 print(f"“{i}”")
#         return
# result = Solution.findTheDifference(Solution,'abc','abce')

# 找出年龄最大者的姓名和年龄
people = {'amy':18, 'kitty':25, 'bob':30, 'recheal':17}
# people_sort=sorted(people.items(),key=lambda x: x[1], reverse=True) #这是按值排序，输出键值对
# print(people_sort[0])
# age_max = float('-inf')
# age_name = 0
# for name, age in people.items():
#     if age > age_max:
#         age_max = age
#         age_name = name
# print(f'年龄最大者是：{age_name}，年龄为{age_max}')

# 给一个数，插入到一个已排序的列表中的正确位置
# list = [5,10,15,20,25,30]
# new_num = int(input('请输入一个整数：')) #因为用户输入的是str，需要转换为int才能才下面进行比较
# for i in range(len(list)):
#     if list[i] > new_num:
#         list.insert(i,new_num)
#         break
# else:
#     list.append(new_num)
# print(list)

# 接受用户输入的三个数字，并按顺序输出
# num1 = float(input('请输入数字一：'))
# num2 = float(input('请输入数字二：'))
# num3 = float(input('请输入数字三：'))
# new_list = sorted([num1, num2, num3])
# print(new_list)

# # 输入一个奇数，找到能被这个数整除的由9组成的最小的数
# num = int(input('Enter a 奇数: '))
# n = 1
# # 循环次数未知，结束条件已知，因此用死循环+break
# while True:
#     number9 = int('9'*n)
#     if number9 % num == 0:
#         print(f'{number9}/{num}={number9/num}')
#         break
#     n += 1

# 判断闰年
# year = int(input('Enter year: '))
# if year % 4 == 0 and year % 100 != 0:
#     print(f'{year} is 闰年')
# elif year % 400 == 0:
#     print(f'{year} is 闰年')
# else:
#     print(f'{year}不是闰年')

#下面是精简版本
# year = int(input('Enter year: '))
# if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#     print(f'{year} is 闰年')
# else:
#     print(f'{year}不是闰年')

# 进制转换
# num = int(input('Enter a number: '))
# print('十进制为：', num)
# print('二进制为：', bin(num))
# print('八进制为：', oct(num))
# print('十六进制为：', hex(num))


# while True:
#     a = float(input('enter a number:'))
#     b = a ** 2
#     print(b)
#     if b < 50:
#         print('结果小于50，程序结束。')
#         break

# 计算题
# num = int(input('Enter a number: '))
# num_times = int(input('Enter times of numbers: '))
# result1 = 0
# result2 = 0
# for i in range(1,num_times+1):
#     result1 = result1*10 + num
#     result2 = result1 + result2
# print(result2)

# #定义函数
# def add(x, y):
#     return x + y
# add(1, 2)
# result

# def factorial(n):
#     total_sum = 1
#     if n == 0:
#         return 1
#     else:
#         for i in range(1,n+1):
#             total_sum= total_sum * i
#         return print(total_sum)
#
# factorial(5)

# 优雅写法
# list1 = [i for i in range(1,11) if i % 2 == 0]
# list2 = ['str'+str(i) for i in range(1,11) if i % 2 == 0]
# list3 = [i**2 for i in range(1,11) if i % 2 == 0]
# print(list3)

# def func(x):
#     return x**2
# list(map(func, range(10)))
# print(list(map(func, range(10)))) map对对象重复执行第一个位置的行为
# list(map(lambda x: x**2, range(1,10))) 匿名函数简化代码，因为x的平方不需要去弄个函数封装起来
# print(list(map(lambda x: x**2, range(1,10))))

# 第三方包
# import collections
# a = [1,2,3,4,5,6,7,8,1,2,3,4,9,5,8]
# b = collections.Counter(a)
# print(b)

# 圆的面积
# def area_of_circle(x):
#     return round(3.14 * x ** 2,2)
#
# x = float(input("enter 半径 of circle: "))
# print(area_of_circle(x))
# Π可以用第三方库math.pi导入，这样精度更高

# 打印指定范围的素数, 函数套用
# def is_sushu(num):
#     """
#     作用：判断是否为素数
#     参数：要判断的值
#     返回值：有，true or false
#     """
#     if num <= 1:
#         return False
#     for i in range(2, num):
#         if num % i == 0:
#             return False
#     return True
#
# def sushu(x,y):
#     """"
#     作用：打印范围内素数
#     参数：范围起始值，范围结束值
#     返回值：无
#     """
#     for i in range(x,y):
#         if is_sushu(i)==True:  #因为这个地方需要重复判断，因此用函数更加简便
#             print(i)
#
# a=sushu(1,10)

# 计算整数平方和
# def int_square(num):
#     """
#     作用：所有整数平方和
#     参数：最后一个整数
#     返回值：结果
#     """
#     sum = 0
#     for i in range(1, num + 1):
#         sum = sum + i ** 2
#         print(sum)
#     return sum
#
# print(int_square(5))

# 列表中所有数字的总和
# def list_sum(number_list):
#     """
#     作用：给定列表中所有数字的总和
#     参数：数字列表
#     返回值：总和
#     """
#     current_sum = 0
#     for i in number_list:
#         current_sum += i
#     return current_sum
#
# print(list_sum([1,2,3,4,5,8,10]))
#更简便方法
# list1=[1,2,3,4,5,8,10]
# print(sum(list1))

# 保存范围内的偶数到列表里
# def oushu(star, end):
#     """
#     作用：将偶数加到列表里
#     :param star:
#     :param end:
#     :return:
#     """
#     oushu_list= []
#     for i in range(star, end+1):
#         if i % 2 == 0:
#             oushu_list.append(i)
#     return oushu_list
#
# print(oushu(100, 200))
# 优雅写法
# def os(start, end):
#     return [i for i in range(start,end) if i % 2 == 0]
# print(os(100, 120))



def build_person(first_name, last_name, age=None):
    """返回一个字典，其中包含有关一个人的信息"""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person
musician = build_person('jimi', 'hendrix')
print(musician)














