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

arr = np.random.randn(1000,3)
arrr = np.split(arr,3,axis=1)
arr_std = arr.std(axis=0)*3
print((arr > arr_std).any(axis=0))

