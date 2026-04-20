from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt


def get_weather_data(path, dates, highs, lows, date_index, high_index,
                     low_index):
    """从数据文件中获取最高温度和最低温度"""
    lines = path.read_text().splitlines()
    reader = csv.reader(lines)
    header_row = next(reader)

    # 提取日期、最高温度和最低温度
    for row in reader:
        current_date = datetime.strptime(row[date_index], '%Y-%m-%d')
        try:
            high = int(row[high_index])
            low = int(row[low_index])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

path = Path('weather_eq_data/sitka_weather_2021_simple.csv')
dates, highs, lows = [], [], []
get_weather_data(path, dates, highs, lows, date_index=2, high_index=4,
                 low_index=5)

# 根据数据度绘图
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, highs, color='red', alpha=0.5)
ax.plot(dates, lows, color='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# 设置绘图的格式
ax.set_title("Daily High and Low Temperatures, 2021", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()