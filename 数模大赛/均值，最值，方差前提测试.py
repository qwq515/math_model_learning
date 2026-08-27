import pandas as pd         #pandas是Python中用于数据分析的库，提供了高性能、易用的数据结构和数据分析工具
import os                   #os模块提供了与操作系统进行交互的功能，如文件和目录操作
os.chdir(os.path.dirname(os.path.abspath(__file__)))        #os.chdir()方法将当前工作目录更改为当前脚本所在的目录，避免路径问题
#读取文件
df = pd.read_csv('合并后的销售数据.csv')
#看看“是否打折”这一行都有哪些可能
print("打印行的唯一值",df['是否打折销售'].unique())     #.unique()方法返回“是否打折销售”这一中所有不同的值
#只保留销量大于0的正常值
df = df[df['销量(千克)']>0]
#剔除打折样本(后来考虑了一下，不能舍弃打折样本)
#df_clean = df[df['是否打折销售']!="是"]
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

result_full = df_clean.groupby('')

result_sorted = result.sort_values(by='方差',ascending=False)        #按方差降序排序,ascending=False表示降序排列
#打印排序过后前10条数据
print('销量波动最大的前10条数据为：')
print(result_sorted.head(10))
#挑出波动最大的前2条数据的单品编码，查看原始数据中的每次销售数据
result_sorted.to_csv('清洗后的销量数据.csv', index=False,encoding='utf-8-sig')        #将结果保存为CSV文件，index=False表示不保存索引列,encoding='utf-8-sig'表示使用UTF-8编码并添加BOM头，确保在Excel中正确显示中文
print('输出完成') 
unstable_codes = result_sorted.head(2)['单品编码'].tolist()        #获取波动最大的前2条数据的单品编码，并转换为列表
unstable_data = df_clean[df_clean['单品编码'].isin(unstable_codes)]##筛选出原始数据中单品编码在unstable_codes列表中的数据,.isin()方法用于判断每个元素是否在指定的列表中
print('销量波动最大的前2条数据的原始销售数据为：')
print(unstable_data)
unstable_data.to_csv('销量波动最大的前2条数据的原始销售数据.csv', index=False,encoding='utf-8-sig')        #将结果保存为CSV文件，index=False表示不保存索引列,encoding='utf-8-sig'表示使用UTF-8编码并添加BOM头，确保在Excel中正确显示中文
#将日期转换成日期类型
df_clean['销售日期'] = pd.to_datetime(df_clean['销售日期'])
#提取年月
df_clean['年月'] = df_clean['销售日期'].dt.to_period('M')       #dt是datetime专用访问器，.to_period('M')方法将日期转换为按月的时间段
#pandas 的规则很简单：
#如果 df_clean['某列'] 已存在 → 赋值时就是 修改
#如果 df_clean['某列'] 不存在 → 赋值时就是 新增
#按“单品编码+年月”再次分组算均值
monthly_trend = df_clean.groupby(['单品编码','年月'])['销量(千克)'].mean().reset_index()
print("按单品编码+年月分组后的均值数据为：")
print(monthly_trend)
monthly_trend.to_csv('按月份分组后各个单品销量.csv',index=False,encoding='utf-8-sig')