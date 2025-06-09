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
# arr = np.random.randint(0,100,size=(3,4))
# index = pd.Index(data=['amy','tom','bob'],name='姓名')
# columns = ['语文','数学','英语','历史']
# df = pd.DataFrame(data=arr,index=index,columns=columns)
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
# df = pd.read_csv('kongzhilianxi.csv',sep=',',header=0,index_col=0)
# print(df)
# 使用 .isnull() 和 .notnull() 检测缺失值。
# print(df.loc[df.isnull().any(axis=1)]) #精准地找出了有缺失值的行，而并不是单纯返回一个bool series或bool dataframe
# print(df.loc[df.notnull().all(axis=1)]) #精准地找出了不含缺失值的行，而并不是...
# 使用 .dropna() 删除包含缺失值的行或列。
# df_new = df.dropna(axis=0,how='any') #删除的是行
# print(df_new)
# 使用 .fillna() 填充缺失值（例如，用 0、均值、中位数等填充）。
# print(df.fillna(value=0))
# print(df.fillna(df.mean())) #这是以列的均值填充
# df_t = df.T
# print(df_t.fillna(value=0))
# print(df_t.fillna(df_t.mean())) #这是以行的均值填充，先转置就行
# 处理重复值：
# 创建一个包含重复行的 DataFrame。
# df1 = pd.DataFrame({'a':[3,2,3], 'b':[4,5,6],'c':[3,4,5],'d':[4,7,8],'e':[4,5,6]})
# df2 = df1.T
# 使用 .duplicated() 检测重复行。
# print(df2.duplicated())
# 使用 .drop_duplicates() 删除重复行，并尝试保留第一个或最后一个重复项。
# print(df2.drop_duplicates(keep='first'))
# 数据类型转换：
# 查看 DataFrame 各列的数据类型。
# df = pd.read_csv('lianxi.txt',sep=',',header=0)
# print(df)
# 使用 .astype() 转换列的数据类型（例如，将字符串转换为数字，将浮点数转换为整数）。
# print(df.loc[:,'年龄'].astype(float))
# 尝试将包含无法转换的值的列转换为数字类型，观察会发生什么。
# print(df.loc[:,'姓名'].astype(int)) #转不了呗
# 字符串操作：
# 创建一个包含字符串的 Series。
# s1 = pd.Series(['amy','bob','lisa'],index=['a','b','c'])
# print(s1)
# 使用 .str 属性访问字符串方法，例如：
# .lower()、.upper()
# print(s1.str.upper())
# .len
# print(s1.str.len())
# .strip()
# print(s1.str.strip()) #删空白用的
# .split()
# print(s1.str.split())
# .contains()
# print(s1.str.contains('bob')) #返回一个bool series
# .replace()
# print(s1.str.replace('bob','bo'))
# 日期时间操作：
# 创建一个包含日期时间字符串的 Series。
# s1 = pd.Series(['2025年4月21日','2025-04-28','2025年5月2日'],index=['a','b','c'])
# print(s1)
# 使用 pd.to_datetime() 将字符串转换为 datetime 对象。
# datetime_series = pd.to_datetime(s1,errors='coerce')
# print(datetime_series)
# 再来个复杂的
# date_strings = pd.Series([
#     '2023-01-15',                  # YYYY-MM-DD
#     '2024/03/22 10:30:00',         # YYYY/MM/DD HH:MM:SS
#     'January 1st, 2023',           # Month Day, Year
#     '15-Feb-2022',                 # DD-Mon-YYYY
#     '2021-07-01 14:05',            # YYYY-MM-DD HH:MM
#     '20200825',                    # YYYYMMDD
#     '2025-06-05T12:00:00Z',        # ISO 8601 format
#     'Invalid Date',                # 一个无法转换的字符串
#     '2023-13-01'                   # 无效的月份
# ])
# datetime_series = pd.to_datetime(date_strings, errors='coerce')
# print(datetime_series)
# 从 datetime Series 中提取年份、月份、日期、小时等。  .dt是个访问器
# s2 = pd.Series(['2025-04-21','2025-04-28','2025-05-02'],index=['a','b','c'])
# s2_datetime = pd.to_datetime(s2)
# print("\n提取年份:")
# print(s2_datetime.dt.year)
# print(s2_datetime.dt.month)
# print(s2_datetime.dt.day)
# 进行日期时间的比较和计算。

# 第三阶段：数据操作和分析 (熟悉分组、聚合、合并、排序等)
# 分组 (GroupBy)：
# 加载一个包含分类数据的 CSV 文件（例如，包含不同部门员工信息的表格）。
# df = pd.read_csv('lianxi.txt',sep=',',header=0)
# 使用 .groupby() 方法按一列或多列进行分组。
# print(df.groupby(by=['性别']))
# 对分组后的数据应用聚合函数（例如，.sum()、.mean()、.count()、.min()、.max()）。
# print(df.groupby(by=['性别']).count())
# 对不同的列应用不同的聚合函数（使用 .agg()）。
# print(df.groupby(by=['性别']).agg({'姓名':np.count_nonzero,'年龄':np.mean}))
# 聚合 (Aggregation)：
# 学习使用 .agg() 对整个 DataFrame 或分组后的 DataFrame 进行多种聚合操作。

# 合并 (Merge)：
# 创建两个具有共同列的 DataFrame。
# df1 = pd.DataFrame(data=np.random.randint(40,100,(3,4)),index=['a','b','c'],columns=['语文','数学','英语','历史'])
# df2 = pd.DataFrame(data=np.random.randint(40,100,(3,4)),index=['d','e','c'],columns=['语文','数学','英语','历史'])
# 使用 pd.merge() 将这两个 DataFrame 按照共同列进行合并（尝试不同的 how 参数：'inner', 'outer', 'left', 'right'）。
# print(pd.concat([df1,df2],axis=0,join='inner'))
# print(pd.merge(left=df1,right=df2,how='outer'))
# 连接 (Concatenate)：
# 创建两个具有相同列或不同列的 DataFrame。
# 使用 pd.concat() 将这两个 DataFrame 沿着行或列方向进行连接。
# 排序 (Sorting)：
# 使用 .sort_values() 按单列或多列对 DataFrame 进行排序（升序和降序）。
# print(df1.sort_values(by='语文'))
# 使用 .sort_index() 按索引对 DataFrame 进行排序。
# print(df2.sort_index(axis=0))
# 数据透视表 (Pivot Table)：
# 使用 pd.pivot_table() 创建数据透视表，对数据进行重塑和聚合。
# 创建dataframe
# data = {
#     'Region': ['East', 'West', 'East', 'West', 'North', 'South', 'East', 'North'],
#     'Salesperson': ['Alice', 'Bob', 'Alice', 'Charlie', 'David', 'Eve', 'Bob', 'David'],
#     'Product': ['Laptop', 'Mouse', 'Keyboard', 'Laptop', 'Mouse', 'Keyboard', 'Laptop', 'Monitor'],
#     'Quantity': [2, 5, 3, 1, 4, 2, 3, 1],
#     'Price': [1200, 25, 75, 1300, 30, 80, 1250, 150],
#     'Date': pd.to_datetime(['2023-01-10', '2023-01-12', '2023-01-15', '2023-01-18',
#                            '2023-02-01', '2023-02-05', '2023-02-10', '2023-02-12'])
# }
# df = pd.DataFrame(data)
# df['Revenue'] = df['Quantity'] * df['Price']
#
# print("原始 DataFrame:")
# print(df)
# print("-" * 50)
# 按区域计算销售额,默认的聚合函数是均值
# pivot1 = pd.pivot_table(df, index='Region', values='Revenue')
# print("\n1. 按区域计算平均销售额:")
# print(pivot1)
# print("-" * 50)
# 按区域计算总销售额
# pivot2 = pd.pivot_table(df,index='Region',values='Revenue',aggfunc='sum')
# print(pivot2)
# 按区域和产品计算总销售额
# pivot3 = pd.pivot_table(df,index='Region',columns='Product',values='Revenue',aggfunc='sum')
# print(pivot3)
# 多级索引和多级列：按区域、销售员和产品计算数量
# pivot4 = pd.pivot_table(df,index=['Region','Salesperson'],columns='Product',values='Quantity',aggfunc='sum')
# print(pivot4)
# pivot5 = pd.pivot_table(df,
#                         index='Region',
#                         aggfunc={
#                             'Quantity': 'sum',      # 对 Quantity 列求和
#                             'Revenue': 'mean',      # 对 Revenue 列求平均
#                             'Product': 'count'      # 对 Product 列计数（非空数量）
#                         })
# print(pivot5)
# 包含小计，margins=True
# pivot7 = pd.pivot_table(df, index='Region', columns='Product', values='Revenue', aggfunc='sum', fill_value=0, margins=True)
# print("\n7. 按区域和产品计算总销售额 (包含总计):")
# print(pivot7)
# print("-" * 50)


# 第四阶段：实践项目 (将所学知识应用于实际问题)
# 分析小型数据集：
# 找一些公开的小型数据集（例如，Kaggle、UCI Machine Learning Repository）。
# 使用 Pandas 加载和清洗数据。
# 进行探索性数据分析（EDA），例如：
# 计算统计指标。
# 可视化数据的分布（可以使用 Matplotlib 或 Seaborn 库）。
# 提出并回答关于数据的有趣问题
