import numpy as np
import pandas as pd
# index=['张三','李四','王五','赵六']
# columns=['Python','Java','C']
# score1 = pd.DataFrame(data=np.random.randint(30,100,size=(4,3)),index=index,columns=columns)
# score2 = pd.DataFrame(data=np.random.randint(30,100,size=(4,3)),index=index,columns=columns)
# # print(score1)
# score_mean = (score1 + score2) / 2
# score1.loc['张三','Java'] = 0
# score1.loc['李四'] += 10
# # print(score1)
# # 找出java成绩比python成绩好的同学，这是我自己写的
# print(score1.where(score1.loc[:,'Java']>score1.loc[:,'Python']))
# # 这是给的答案
# cond2 = score1['Python'] < score1['Java']
# print(score1.loc[cond2].index)

# index = ['lucy','tom','jack']
# level1 = ['期中','期末']
# level2 = ['Python','Java','C']
# columns = pd.MultiIndex.from_product([level1,level2])
# data = np.random.randint(30,100,size=(3,6))
# score_total = pd.DataFrame(data=data,index=index,columns=columns)
# print(score_total)
# 求lucy最高分是哪一门课
# print(score_total.loc['lucy',score_total.loc['lucy'] == np.max(score_total.loc['lucy'])])
# 这就是df.loc[row,columns]的用法，此处的row是行标签lucy，列标签是为True的bool
# 求tom期中期末每门的平均成绩
# s1 = score_total.loc['tom']
# s11 = s1.unstack()
# print(s11.mean())
# 给tom期中的python加20分
# score_total.loc['jack',('期中','Python')] += 20
# print(score_total)


# 第一阶段：Series 和 DataFrame 的基本操作 (熟悉创建、查看和简单选择数据)
# 创建 Series 和 DataFrame：
# 从一个 Python 列表创建一个 Pandas Series。
# list = ['amy','tom','bob','lisa']
# list2 = ['101','102','103','104']
# s1 = pd.Series(data=list,index=list2)
# print(s1)
# 从一个 Python 字典创建一个 Pandas Series。
# dic = {'101':'amy','102':'tom','103':'bob','104':'lisa'}
# s1 = pd.Series(data=dic)
# print(s1)
# 从一个 Python 字典列表创建一个 Pandas DataFrame。
# names = ['amy','tom','bob']
# age = np.random.randint(18,25,size=3)
# level = np.random.randint(1,3,size=3)
# info = {'name':names,'age':age,'level':level}
# df = pd.DataFrame(data=info,index=[1,2,3])
# print(df)
# 从一个 NumPy 数组创建一个 Pandas DataFrame，并指定列名。
# arr = np.random.randint(0,100,size=(3,4))
# index = ['amy','tom','bob']
# columns = ['语文','数学','英语','历史']
# df = pd.DataFrame(data=arr,index=index,columns=columns)
# print(df)
# 创建一个空的 Pandas DataFrame。
# df = pd.DataFrame(data=None,index=list('ABCD'),columns=['姓名','年龄','地址','联系方式'])
# print(df)
# 查看 DataFrame 的基本信息：
# 加载一个简单的 CSV 文件（例如，你可以自己创建一个包含几行数据的 CSV 文件）
# df = pd.read_csv('lianxi.txt',sep=',',header=0)
# 使用 .head() 查看 DataFrame 的前几行。
# print(df.head(5))
# 使用 .tail() 查看 DataFrame 的后几行。
# print(df.tail(5))
# 使用 .info() 查看 DataFrame 的基本信息（索引、数据类型、非空值等）。
# print(df.info())
# print(df.sample(3))
# 使用 .describe() 查看 DataFrame 的统计摘要（计数、均值、标准差等）。
# print(df.describe())
# 使用 .shape 查看 DataFrame 的维度。
# print(df.shape)
# 使用 .columns 查看 DataFrame 的列名。
# print(df.columns)
# 使用 .index 查看 DataFrame 的索引。
# print(df.index)
# 使用 .dtypes 查看 DataFrame 每列的数据类型。
# print(df.dtypes)
# 选择数据：
arr = np.random.randint(0,100,size=(3,4))
index = pd.Index(data=['amy','tom','bob'],name='姓名')
columns = ['语文','数学','英语','历史']
df = pd.DataFrame(data=arr,index=index,columns=columns)
# 选择 DataFrame 中的单列（使用列名）。
# print(df['语文'])
# print(df.loc[:,'语文'])
# 选择 DataFrame 中的多列（使用列名列表）。
# print(df[['语文','数学']])
# print(df.loc[:,'语文':'英语'])
# 使用 .loc[] 按标签选择行和列，上面做过了
# 选择特定的行（例如，第一行、最后一行）。
# print(df.head(1))
# print(df.tail(1))
# 选择特定的列。
# print(df[df.columns[0]])
# 选择特定的行和列的交叉部分。
# print(df.loc['tom','历史'])
# 使用标签切片选择行和列的范围，上面做过了
# 使用 .iloc[] 按整数位置选择行和列：
# print(df.iloc[1])
# print(df.iloc[:,1])
# 选择特定的行（例如，索引为 0 的行，位置概念要用iloc）。
# print(df.iloc[0])
# 选择特定的列（例如，索引为 0 的列）。
# print(df.iloc[:,0])
# print(df.columns[0])
# 使用整数切片选择行和列的范围。
# print(df.loc['amy':'tom','数学':'历史'])
# 使用布尔索引选择满足特定条件的行：
# cond = df>60
# print(df[np.all(cond,axis=1)])
# 选择某一列中值大于某个值的行。
# cond = df['语文']>60
# print(df.loc[cond])
# 选择某一列中值等于某个值的行。
# 使用多个条件进行选择（使用 & 和 | 运算符），两种表达是一样的。
# cond = (df['语文']>60) | (df['数学']>60) | (df['英语']>60)
# print(df.loc[cond])
# print(df[cond])

# 第二阶段：数据清洗和处理 (熟悉处理缺失值、重复值、数据类型转换等)
# 处理缺失值：
# 加载一个包含缺失值的 CSV 文件（你可以手动在 CSV 文件中添加一些空值）。
# 使用 .isnull() 和 .notnull() 检测缺失值。
# 使用 .dropna() 删除包含缺失值的行或列。
# 使用 .fillna() 填充缺失值（例如，用 0、均值、中位数等填充）。
# 处理重复值：
# 创建一个包含重复行的 DataFrame。
# 使用 .duplicated() 检测重复行。
# 使用 .drop_duplicates() 删除重复行，并尝试保留第一个或最后一个重复项。
# 数据类型转换：
# 查看 DataFrame 各列的数据类型。
# 使用 .astype() 转换列的数据类型（例如，将字符串转换为数字，将浮点数转换为整数）。
# 尝试将包含无法转换的值的列转换为数字类型，观察会发生什么。
# 字符串操作：
# 创建一个包含字符串的 Series。
# 使用 .str 属性访问字符串方法，例如：
# .lower()、.upper()
# .len()
# .strip()
# .split()
# .contains()
# .replace()
# 日期时间操作：
# 创建一个包含日期时间字符串的 Series。
# 使用 pd.to_datetime() 将字符串转换为 datetime 对象。
# 从 datetime Series 中提取年份、月份、日期、小时等。
# 进行日期时间的比较和计算。

# 第三阶段：数据操作和分析 (熟悉分组、聚合、合并、排序等)
# 分组 (GroupBy)：
# 加载一个包含分类数据的 CSV 文件（例如，包含不同部门员工信息的表格）。
# 使用 .groupby() 方法按一列或多列进行分组。
# 对分组后的数据应用聚合函数（例如，.sum()、.mean()、.count()、.min()、.max()）。
# 对不同的列应用不同的聚合函数（使用 .agg()）。
# 聚合 (Aggregation)：
# 学习使用 .agg() 对整个 DataFrame 或分组后的 DataFrame 进行多种聚合操作。
# 合并 (Merge)：
# 创建两个具有共同列的 DataFrame。
# 使用 pd.merge() 将这两个 DataFrame 按照共同列进行合并（尝试不同的 how 参数：'inner', 'outer', 'left', 'right'）。
# 连接 (Concatenate)：
# 创建两个具有相同列或不同列的 DataFrame。
# 使用 pd.concat() 将这两个 DataFrame 沿着行或列方向进行连接。
# 排序 (Sorting)：
# 使用 .sort_values() 按单列或多列对 DataFrame 进行排序（升序和降序）。
# 使用 .sort_index() 按索引对 DataFrame 进行排序。
# 数据透视表 (Pivot Table)：
# 使用 pd.pivot_table() 创建数据透视表，对数据进行重塑和聚合。

# 第四阶段：实践项目 (将所学知识应用于实际问题)
# 分析小型数据集：
# 找一些公开的小型数据集（例如，Kaggle、UCI Machine Learning Repository）。
# 使用 Pandas 加载和清洗数据。
# 进行探索性数据分析（EDA），例如：
# 计算统计指标。
# 可视化数据的分布（可以使用 Matplotlib 或 Seaborn 库）。
# 提出并回答关于数据的有趣问题
