import pandas as pd

file1 = "数模大赛/附件1.csv"
file2 = "数模大赛/附件2.csv"

# 读取附件
# 单品编码按文字读取，避免编码被程序改成科学计数法
df1 = pd.read_csv(file1, dtype={"单品编码": str})
df2 = pd.read_csv(
    file2,
    dtype={"单品编码": str},
    low_memory=False
)

print("========== 附件1 ==========")

print("数据尺寸：", df1.shape)

print("\n字段名：")
print(df1.columns.tolist())

print("\n前5行：")
print(df1.head())

print("\n数据类型：")
print(df1.dtypes)


print("\n\n========== 附件2 ==========")

print("数据尺寸：", df2.shape)

print("\n字段名：")
print(df2.columns.tolist())

print("\n前5行：")
print(df2.head())

print("\n数据类型：")
print(df2.dtypes)