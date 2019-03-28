#!/usr/bin/env python
# coding: utf-8

# In[63]:


import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
import locale

# read csv
data = pd.read_csv('/Users/yan/PYTHON/ML/75b640397916e1d9ed2e308abbc0eb7b_export.csv')

# Chinese 
mpl.rc('font', family='Arial Unicode MS')

# use the code below to roughly find the Chinese font we have (Chinese font mostly got bigger file)
'''
from matplotlib.font_manager import fontManager
import os

fonts = [font.name for font in fontManager.ttflist if
         os.path.exists(font.fname) and os.stat(font.fname).st_size > 1e6]

for font in fonts:
    print(font)
'''

# fix coma problem
locale.setlocale(locale.LC_NUMERIC, '')
data['外籍旅客人數'] = data['外籍旅客人數'].apply(locale.atof)
data['華僑旅客人數'] = data['華僑旅客人數'].apply(locale.atof)

# 外籍旅客人數歷年變化圖
data[:].plot.bar(x='年別', y=['外籍旅客人數'],  figsize=(25,15), title = '外籍旅客人數歷年變化圖', fontsize =16)

# 華僑旅客人數歷年變化圖
data[:].plot.bar(x='年別', y=['華僑旅客人數'],  figsize=(25,15), title = '華僑旅客人數歷年變化圖', fontsize =16)

# show
print(data.head())





# In[37]:





# In[ ]:





# In[ ]:




