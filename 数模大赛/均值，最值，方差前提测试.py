import pandas as pd
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
#读取文件
df = pd.read_csv('附件2.csv')
#看看“是否打折”这一行都有哪些可能
print("打印行的唯一值",df['是否打折销售'].unique())
#只保留销量大于0的正常值
df = df[df['销量']>0]
#剔除打折样本
df_clean = df[df['是否打折销售']!="是"]

