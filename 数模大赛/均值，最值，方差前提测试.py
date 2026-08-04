import pandas as pd
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
#读取文件
df = pd.read_csv('附件2.csv')
#看看“是否打折”这一行都有哪些可能
print("打印行的唯一值",df['是否打折销售'].unique())
#只保留销量大于0的正常值
df = df[df['销量(千克)']>0]
#剔除打折样本
df_clean = df[df['是否打折销售']!="是"]
#按“单品编码”分组，计算每个单品的平均销量、最大销量、最小销量和方差
result = df_clean.groupby('单品编码').agg(      #.groupby()方法按“单品编码”分组，.agg()方法对每个分组进行聚合计算
    样本数量=('销量(千克)', 'count'),
    平均销量=('销量(千克)', 'mean'),
    最大销量=('销量(千克)', 'max'),
    最小销量=('销量(千克)', 'min'),
    方差=('销量(千克)', 'var')
).reset_index()                 #.reset_index()方法将分组后的索引重置为默认整数索引,删了影响不大
#打印结果
print(result)
    