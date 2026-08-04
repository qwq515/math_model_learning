import pandas as pd         #导入pandas库，并给他起个名字pd
#读取Excel文件
df = pd.read_excel('附件2.xlsx')      #数据保存在df这个“表格”里
#打印表格前几行，检查是否读取成功
print(df.head())