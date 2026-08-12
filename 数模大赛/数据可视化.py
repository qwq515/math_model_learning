import matplotlib.pyplot as plt  # 导入matplotlib.pyplot模块，用于绘制图表
import seaborn as sns # 导入seaborn模块，用于数据可视化
#1.解决中文乱码，必须加
plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置字体为SimHei以支持中文显示
plt.rcParams['axes.unicode_minus'] = False  # 正常显示负号
#2.设置图表大小
plt.figure(figsize=(10, 6))  # 设置图表大小为10英寸宽，6英寸高