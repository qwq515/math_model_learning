import pandas as pd
#此处只搬运，不计算
df = pd.read_excel('附件4.xlsx' ,engine='openpyxl')  
    #保存为CSV（读取速度快）                                                        
df.to_csv('附件4.csv',index=False,encoding='utf-8-sig')

print(df.head())
print(df.shape)
print("转换完成")