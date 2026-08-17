import pandas as pd
# 读取合并后的销售数据（指定编码避免中文乱码）
df = pd.read_csv('合并后的销售数据.csv', encoding='utf-8-sig')

# 筛选销售类型为「退货」的记录
returns = df[df['销售类型'] == '退货']

# 输出结果
print(f"共找到 {len(returns)} 条退货记录")      #f用于格式化输出，{len(returns)}表示退货记录的数量
print("退货记录所在的行号（DataFrame索引，对应Excel行号需加2：1行表头+从0开始）：")
print(returns.index.tolist())
print("\n退货记录的详细信息：")
print(returns.to_string())

#无所谓，退货的销售值是负的，被当成异常数据清洗了