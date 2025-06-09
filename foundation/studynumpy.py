from datetime import date

import numpy as np
# arr1 = np.random.randint(-5,5,size=(3,4))
# arr2 = np.linspace(0,15,5,endpoint=False)
# arr3 = np.arange(0,15,3)
# arr4 = np.random.random(size=(100,100,3))
# data = arr4
# c = 2*np.pi
# arr5 = np.linspace(0,c,8,endpoint=False)
# arr6 = np.random.randint(0,100,size=10)

# 输出列值
# 方法一
# arr7 = np.random.randint(0,100,size=(5,4))
# print(arr7[:,[2,3]])
# 方法二
# print(arr7[:,-2:])
# 方法三
# print(arr7[:,[False,False,True,True]])

# arr8 = np.random.randint(0,10,size=(4,4))
# arr9 = np.random.randint(0,10,size=(8,4))
# arr10 = np.concatenate((arr8, arr9), axis=0)
# arr11 = np.split(arr10,[1,4])
# arr12 = np.split(arr10,3)
# print(arr12)
# 转换元素类型
# arr13 = np.random.randint(1,10,size=5)
# print(arr13.astype(np.float32))

# a = np.ones((4,1))
# b = np.arange(4)
# print(a+b)

# score = np.random.randint(50,100,100)
# sixty = (score > 60).astype(np.int8)
# print(np.mean(sixty))

# arr = np.random.randn(1000,3)
# arrr = np.split(arr,3,axis=1)
# arr_std = arr.std(axis=0)*3
# print((arr > arr_std).any(axis=0))

# arr = np.zeros((10,10))
# print(arr)

# 第一阶段：基础操作 (熟悉 NumPy 数组的创建、属性和基本操作)
# 创建数组：
# 创建一个包含数字 0 到 9 的 NumPy 数组。
# list=[]
# for i in range(0,10):
#     list.append(i)
# arr1 = np.array(list)
# print(arr1)
# 创建一个形状为 (3, 3) 的全零数组。
# arr2 = np.zeros((3,3))
# print(arr2)
# 创建一个形状为 (2, 2) 的全一数组。
# arr3 = np.ones((2,2))
# print(arr3)
# 创建一个形状为 (4, 5) 的由随机整数组成的数组（例如，范围在 0 到 10 之间）。
# print(np.random.randint(0,10,size=(4,5)))
# 创建一个单位矩阵（对角线为 1，其余为 0）形状为 (5, 5)
# print(np.eye(3,k=-1))
# 创建一个包含等间隔数字的数组，从 0 开始，到 1 结束，包含 5 个元素。
# print(np.linspace(0,1,5,endpoint=False))
# 创建一个包含等间隔数字的数组，从 2 开始，到 10 结束，步长为 2。
# print(np.arange(2,10,2))
# 数组属性：
# 创建一个随机的二维数组，并打印它的形状（shape）、数据类型（dtype）和维度（ndim）。
# arr = np.random.random(size=(3,4))
# print(arr.shape, arr.dtype,arr.ndim)
# 创建一个一维数组，并尝试改变它的形状为 (2, ?) 或 (?, 3)，观察 reshape 函数的作用。
# arr = np.random.randint(1,10,(2,3))
# print(arr.reshape(3,2))
# 索引和切片：
# 创建一个包含数字 10 到 19 的一维数组，并获取：
# arr = np.array(range(10,20))
# 第一个元素。
# print(arr[0])
# 最后一个元素。
# print(arr[-1])
# 索引为 3 到 7 的元素。
# print(arr[[range(3,8)]]) #这是传入了一个ndarray
# print(arr[range(3,8)]) #这是传入了列表
# print(arr[3:8:1]) #这是用切片
# 每隔一个元素。
# print(arr)
# print(arr[::2])
# 数组的反向。
# print(arr)
# print(arr[::-1])
# 创建一个形状为 (4, 4) 的二维数组，并获取：
# arr = np.random.randint(0,20,size=(4,4))
# print(arr)
# 第一行。
# print(arr[0])
# 最后一列。
# print(arr[:,-1])
# 左上角的 2x2 子数组。
# print(arr[:2,:2]) #逗号前是对行的切片，后是对列切片
# 所有行的第三个元素。
# print(arr[:,2:3])
# 使用布尔索引选择大于 5 的元素（假设数组包含一些大于 5 的元素）。
# print(arr[arr>5])
# 基本运算：
# 创建两个形状相同的随机整数数组，对它们进行加、减、乘、除运算。
# arr1 = np.random.randint(1,10,size=(2,3))
# arr2 = np.random.randint(10,20,size=(2,3))
# print(arr1)
# print(arr2)
# print(arr1*arr2)
# 创建一个数组，并对它进行标量运算（例如，乘以 2，加上 5，取平方）。
# arr1 = np.random.randint(1,10,size=(2,3))
# print(arr1)
# print((arr1*2+5)**2)
# 尝试对形状不匹配的数组进行运算，观察 NumPy 的广播机制（可以先查阅相关资料）。
# arr1 = np.random.randint(0,10,size=(2,2,2))
# arr2 = np.random.randint(0,10,size=(3,4))
# arr3 = np.arange(3)
# arr4 = np.arange(3).reshape(3,1)
# print(arr3)
# print(arr4)
# arr5 = np.random.randint(0,10,size=(2,2))
# print(arr1)
# print(arr5)
# print(arr1 + arr5)

# 第二阶段：常用函数 (熟悉 NumPy 的通用函数、聚合函数和线性代数基础)
# 通用函数 (ufunc)：
# 创建一个包含一些负数的数组，并计算它们的绝对值。
# arr = np.arange(-10,10)
# arrnew = arr.reshape(4,5)
# print(arrnew)
# print(np.abs(arrnew))
# 创建一个包含浮点数的数组，并计算它们的平方根、指数和对数。
# arr = np.arange(0.5,5.5,0.5).reshape(2,5)
# arr3 = np.array([4,16,25,36,49,64]).reshape(2,3)
# # print(np.power(arr3,0.5))
# # print(np.exp(arr3))
# print(np.log(arr))
# 创建两个数组，并计算它们的元素级最大值和最小值。
# np.maximum(这里面写你要比较的数组)
# 聚合函数：
# 创建一个随机数组，并计算它的总和、最小值、最大值和平均值。
# arr = np.arange(0.5,5.5,0.5).reshape(2,5)
# arr3 = np.array([4,16,25,36,49,64]).reshape(2,3)
# print(np.max(arr))
# print(np.min(arr3))
# print(np.sum(arr))
# print(np.mean(arr3))
# 创建一个二维数组，并分别计算每一列和每一行的总和、最小值和最大值。
# arr = np.random.randint(0,10,size=(3,4))
# print(arr)
# # print(np.sum(arr,axis=0)) #在末尾出结果，也就是按列计算
# # print(np.sum(arr,axis=1)) #出的是右边的结果，也就是按行计算
# print(np.min(arr,axis=0))
# 创建一个布尔数组，并计算 True 元素的个数。
# arr = np.random.randint(0,100,size=(3,4))
# arr1 = np.array(arr>50)
# print(arr1)
# print(np.count_nonzero(arr1))
# 线性代数基础：
# 创建两个二维数组（矩阵），并进行矩阵乘法运算。
# arr1 = np.random.randint(0,100,size=(2,2))
# arr2 = np.random.randint(0,100,size=(2,2))
# arr3 = np.random.randint(0,100,size=(3,4))
# arr4 = np.random.randint(0,100,size=(2,))
# print(arr4)
# print(arr1 + arr4)
# print(np.dot(arr1, arr4))
# 创建一个方阵，并计算它的转置。
# arr = np.random.randint(0,10,size=(5,5))
# print(arr,arr.transpose())
# （进阶）尝试计算一个方阵的行列式和逆矩阵（可以使用 np.linalg 模块）。
# arr = np.random.randint(0,10,size=(5,5))
# print(arr)
# print(np.linalg.det(arr))
# print(np.linalg.inv(arr))
# 第三阶段：进阶操作 (熟悉数组操作、广播机制和实际应用)
# 数组操作：
# 创建两个一维数组，并将它们水平和垂直堆叠起来。
# arr1 = np.random.randint(0,10,size=(3,2))
# arr2 = np.random.randint(0,10,size=(3,2))
# print(np.concatenate((arr1,arr2),axis=0))
# print(np.concatenate((arr1,arr2),axis=1))
# 创建一个二维数组，并将其分割成两个或多个子数组（水平和垂直方向）。
# arr1 = np.random.randint(0,10,size=(3,2))
# print(np.split(arr1,3))
# arr1 = np.random.randint(0,10,size=(5,4))
# print(arr1)
# # print(np.split(arr1,2,axis=1)) #拆成5*2的两个数组了
# print(np.split(arr1,[1,3])) #行0为一组，行1到行2一组，行3到行4一组 数字为索引
# print(np.split(arr1,[1,4],axis=1))
# 创建一个数组，并在其开头、中间和结尾添加新的维度。
# arr = np.array([[1,2,3,4],[3,4,5,6],[5,6,7,8]])
# arr1 = np.append(arr,[[9,8,7,10]],axis=0) #在末尾添加,注意方括号的数量，要指定轴
# arr2 = np.append(arr,[[9],[8],[7]],axis=1) #在右边末尾添加
# arr3 = np.expand_dims(arr,0)
# arr4 = np.expand_dims(arr,1) #这道题的增加维度不太清楚，下面还是按照增加行列来做
# arr5 = np.array([[1,2,3,4]])
# print(np.r_[arr,arr5]) 增加列不是r是c
# arr6 = np.array([[1,2,3,4]])
# print(np.insert(arr,0,arr6,axis=0))
# arr7 = np.array([[1,2,3]])
# print(np.insert(arr,2,arr7,axis=1)) #在第三列增加一列
# 删除数组中的特定行或列。
# arr = np.array([[1,2,3,4],[3,4,5,6],[5,6,7,8],[7,8,9,10]])
# # print(np.delete(arr, 0,axis=0))
# # print(np.delete(arr, 2,axis=1))
# print(np.delete(arr, [range(0,3)],axis=0)) #删除复数行或列
# 广播 (Broadcasting)：
# 创建一个形状为 (3, 1) 的数组和一个形状为 (1, 4) 的数组，并将它们相加，理解广播的规则。
# 创建一个形状为 (3,) 的数组和一个标量，并将它们相加。
# 实际应用 (小练习)：
# 计算平均值和标准差： 给定一个包含学生考试分数的 NumPy 数组，计算所有学生的平均分和标准差。
# student_exam = np.random.randint(40,100,50)
# print(f'学生的平均分为{np.mean(student_exam)},标准差为{np.std(student_exam)}')
# 归一化数据： 给定一个包含一组特征数据的 NumPy 数组，将其归一化到 0 到 1 的范围（使用最小值和最大值）。
# def minmax_normalize(data):
#     """
#     参数：数组
#     作用：归一化
#     有返回值
#     """
#     data_max=np.max(data)
#     data_min=np.min(data)
#     # if data_max == data_min:
#     #     print("警告：检测到恒定值数组，返回零矩阵")
#     #     return np.zeros_like(data)
#     if data_max == data_min:
#         print("警告：检测到恒定值数组，返回零矩阵")
#         return np.zeros_like(data)
#     normalized = (data - data_min) / (data_max - data_min)
#     return normalized
# print(minmax_normalize([3,3,3]))
# 距离计算： 给定两个表示点的 NumPy 数组（例如，二维坐标），计算它们之间的欧几里得距离。
# 简单的图像处理： 加载一个简单的灰度图像（可以表示为一个二维 NumPy 数组），尝试对其进行一些基本操作，例如调整亮度（加上一个常数）、对比度（乘以一个常数）。


