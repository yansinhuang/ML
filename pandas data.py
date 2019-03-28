import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import locale
data = pd.read_csv('75b640397916e1d9ed2e308abbc0eb7b_export.csv')

# fix coma problem
locale.setlocale(locale.LC_NUMERIC, '')
data['外籍旅客人數'] = data['外籍旅客人數'].apply(locale.atof)

data[:20].plot.bar(x='年別', y=['外籍旅客人數'])

print(data.head())




