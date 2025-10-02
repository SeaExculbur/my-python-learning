name = "公司"
stock_price = 50
stock_code = "0809"
stock_price_daily_growth_factor = 1.25
grow_days = 5
print(f"name , 股票代码 , {stock_code} , 当前票价 , {stock_price}")
print("每日增长系数是:%.1f, 经过%d天增长后，, 股价达到了%.3f" % (stock_price_daily_growth_factor , grow_days , stock_price * stock_price_daily_growth_factor ** grow_days))