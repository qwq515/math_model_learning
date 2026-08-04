import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

plt.rcParams['font.sans-serif'] = ['SimHei']   # 中文显示
plt.rcParams['axes.unicode_minus'] = False     # 负号显示

# 1. 读数据
df_sales = pd.read_excel('附件2.xlsx')   # 销售流水
df_info  = pd.read_excel('附件1.xlsx')   # 商品信息

# 2. 看结构（拿到数据第一件事）
print(df_sales.info())
print(df_sales.head())

# 3. 日期列转成时间类型
df_sales['销售日期'] = pd.to_datetime(df_sales['销售日期'])

# 4. 关联商品信息表，拿到品类列
df = pd.merge(df_sales, df_info, on='单品编码', how='left')

# 5. 按品类+日期聚合每日销量（问题1的核心一步）
daily = df.groupby(['品类', '销售日期'])['销量(kg)'].sum().reset_index()

# 6. 画各品类的销量时间序列
plt.figure(figsize=(12, 5))
for cat in daily['品类'].unique():
    sub = daily[daily['品类'] == cat]
    plt.plot(sub['销售日期'], sub['销量(kg)'], label=cat)
plt.legend()
plt.title('各品类每日销量走势')
plt.show()

# 7. 品类间相关性热力图（先透视成 日期×品类 的宽表）
pivot = daily.pivot(index='销售日期', columns='品类', values='销量(kg)')
corr = pivot.corr(method='spearman')   # 销量数据用 Spearman 更稳
sns.heatmap(corr, annot=True, cmap='RdBu_r')
plt.title('品类销量相关性')
plt.show()
