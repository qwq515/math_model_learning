import pandas as pd
#此处只搬运，不计算
file = ['附件1.xlsx','附件4.xlsx']
for i in file:
    df = pd.read_excel(i,engine='openpyxl')  
    #保存为CSV（读取速度快）
    df.to_csv(i.replace('.xlsx', '.csv'),index=False,encoding='utf-8-sig')

print("转换完成")