import pandas as pd
#此处只搬运，不计算
df = pd.read_excel('附件2.xlsx',engine='openpyxl')
#保存为CSV（读取速度快）
df.to_csv('附件2.csv',index=False,encoding='utf-8-sig')
print("转换完成")