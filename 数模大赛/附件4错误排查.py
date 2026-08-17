import pandas as pd

file = '附件4.xlsx'

print("文件里所有Sheet：")
print(pd.ExcelFile(file).sheet_names)

df = pd.read_excel(file,sheet_name="Sheet1")

print("\n数据大小：")
print(df.shape)

print("\n列名：")
print(df.columns.tolist())

print("\n前5行数据：")
print(df.head())

      