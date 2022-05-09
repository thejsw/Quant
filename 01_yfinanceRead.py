from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override()


sec = pdr.get_data_yahoo('005930.KS', start='2022-05-01')
msft = pdr.get_data_yahoo('MSFT', start='2022-05-01')

print('--------------------------------')
print('Samsung Electronics Co., Ltd. (005930.KS)')
print(sec.head(10))
print('--------------------------------')
print('Microsoft (NASDAQ: MSFT)')
print(msft.head(10))