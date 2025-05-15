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

