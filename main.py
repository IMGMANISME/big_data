import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
plt.rcParams['axes.unicode_minus'] = False

# Read the CSV files into DataFrames
data = pd.read_csv('歷年取締違規分析統計.csv')
data2 = pd.read_csv('國道交通事故百萬車公里統計.csv')

# delete the column of data
del data['行駛路肩']
del data['超速']
del data['大客車站立乘客']
del data['超載']
del data['路肩上下客']
del data['無照駕駛']
del data['酒後駕車']
del data['不依規定車道行駛']
del data['任意停車或未擺警告標誌']
del data['任意變換車道']
del data['載貨未覆蓋沿途滲漏飛散']
del data['裝載不穩妥']
del data['裝載危險物品未依規定']
del data['號牌粘貼反光紙塗抹磨損不清或未依規定縣掛號牌']
del data['未保持行車安全距離']
del data['其他違規']

# delete the column of data2
del data2['百萬車公里']
del data2['肇事率']
del data2['死亡率']
del data2['受傷人數']
del data2['受傷率']
del data2['死亡人數']

# Rename the column[事故發生件數] of data2
data2['事故發生件數'] = data2['發生件數']
del data2['發生件數']


# Divide the data of data by 1000
data['合計取締數/10000'] = data['合計取締數']/10000
del data['合計取締數']

# Print the column names
print(data.to_string())
print(data2.to_string())

# Append the data from the second CSV file to the data from the first CSV file
data = data.append(data2)

# Plot the data from the first CSV file and compare it with the data from the second CSV file
data.plot(x='年別', kind='line')

# Set the x-axis label, y-axis label, and the chart title
plt.xlabel('年')
plt.ylabel('數量')
plt.title('交通事故數與取締數相關圖表')
plt.legend()
plt.savefig('output.png')
plt.show()
