from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override()

aapl = pdr.get_data_yahoo('AAPL', start='2021-05-01')
msft = pdr.get_data_yahoo('MSFT', start='2021-05-01')


import matplotlib.pyplot as plt

plt.plot(aapl.index, aapl.Close, 'b', label='Apple Inc.')
plt.plot(msft.index, msft.Close, 'r--', label='Microsoft Corp.')
plt.legend(loc='best')
plt.show()