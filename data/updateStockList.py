import tushare as ts

df = ts.get_stock_basics()
df.to_csv('data/stockList.csv', encoding="utf-8")
