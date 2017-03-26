# -*- coding: utf-8 -*-
#Python in Finance p107

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.finance as mpf

start = (2014, 5, 1)
end = (2014, 6, 30)
quotes = mpf.quotes_historical_yahoo_ohlc('^GDAXI', start, end)
#quotes = mpf.quotes_historical_yahoo(‘^GDAXI’, start, end)
quotes[:2]
print("quotes = ", quotes[:2])

fig, ax = plt.subplots(figsize=(8, 5))
fig.subplots_adjust(bottom=0.2)

print("Hello")
#use Line2d
#mpf.plot_day_summary_oclh(ax, quotes, ticksize=3, colorup=’k’, colordown=’r’)#
mpf.candlestick_ohlc(ax, quotes, width=0.6, colorup='b', colordown='r')
#mpf.candlestick(ax, quotes, width=0.6, colorup=’b’, colordown=’r’)
plt.grid(True)
ax.xaxis_date()
# dates on the x-axis
ax.autoscale_view()

plt.setp(plt.gca().get_xticklabels(), rotation=30)
plt.show()
#raw_input(“Press Enter to continue…”)
print("bye")
