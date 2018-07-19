import tushare as ts


df_daily =  ts.get_k_data('000001', index=True, start='2018-07-18', end='2018-07-20')
print(df_daily)