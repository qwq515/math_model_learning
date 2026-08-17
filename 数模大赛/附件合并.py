import pandas as pd

# 读取附件1（产品信息表）
df1 = pd.read_csv('附件1.csv', dtype=str)   #dtype=str 表示将所有列都作为字符串处理，避免数值类型转换

# 读取附件2（销售明细表）
df2 = pd.read_csv('附件2.csv', dtype=str)

# 以单品编码为键，进行左连接（保留附件2的所有行，匹配附件1的信息）
merged_df = pd.merge(df2, df1, on='单品编码', how='left')

# 调整列顺序，将产品信息放在单品编码后面
cols = ['销售日期', '扫码销售时间', '单品编码', '单品名称', '分类编码', '分类名称', 
        '销量(千克)', '销售单价(元/千克)', '销售类型', '是否打折销售']
merged_df = merged_df[cols]

# 保存为新的CSV文件
output_path = r'c:\Users\peng\Desktop\一缺抱憾亭\数模大赛\合并后的销售数据.csv'
merged_df.to_csv(output_path, index=False, encoding='utf-8-sig')

print(f"合并完成！共 {len(merged_df)} 条记录")
print(f"文件已保存至：{output_path}")
print("\n前5行预览：")
print(merged_df.head())