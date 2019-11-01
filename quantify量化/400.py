# coding=utf-8

import pandas as pd
# import matplotlib.pyplot as plt
pd.set_option("expand_frame_repr", False)


stock_data = pd.read_csv('/Users/study/caiNiao/wifi/all_trading_data/stock_data.csv', encoding='utf-8')
stock_data.columns = [i for i in stock_data.columns]
stock_data['date'] = pd.to_datetime(stock_data['date'])

stock_data.sort_values(by=['date', 'code'], inplace=True)

# 开始时间太早
stock_data = stock_data[stock_data['date'] > pd.to_datetime('20140104')]
print(stock_data)
exit()

# 将月末停牌股票去除
stock_data = stock_data[stock_data['volume'] != 0]
# 该月交易时间过短， 去除
# 停牌时间过长 也不能买入
stock_data = [stock_data[stock_data['交易天数'] >= 10]]
# 当天涨停的股票也不能买入
stock_data = stock_data[stock_data['最后一天涨跌幅'] <= 0.097]

# 计算所有股票在下个月的平均涨幅
output = pd.DataFrame()
output['所有股票下月涨幅'] = stock_data.groupby('date')['下月涨幅'].mean()
output.to_csv()
