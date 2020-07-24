#!/usr/bin/env python
# coding: utf-8

# In[13]:


import pandas as pd
import yfinance as yf
from yahoofinancials import YahooFinancials


# In[14]:


with open(r'C:\Users\chenxun2\hk.txt', 'r') as f:
    cont = f.readlines()


# In[15]:


stocks = []
for stock in cont:
    stocks.append(stock.strip())


# In[16]:


cnt = 0
res = []
for stock in stocks:
    test=yf.Tickers(stock)
    for ticker in test.tickers:
        try:
            df = ticker.history(period="max")
            res.append(df.iloc[0])
            res.append(ticker)
            #print(res)
        except:
            break
    cnt += 1
    if cnt%10 == 0:
        print(cnt)


# In[17]:


info = []
for i in range(0, len(res)):
    if i % 2 == 0:
        info.append(res[i])


# In[18]:


info = pd.DataFrame(info)


# In[19]:


symbol = []
for i in range(0, len(res)):
    if i % 2 != 0:
        symbol.append(res[i])


# In[20]:


import numpy as np
symbol = np.array(symbol)


# In[21]:


info['symbol'] = symbol


# In[22]:


info.to_excel(r'C:\Users\chenxun2\hk.xlsx')


# In[23]:


results = {}
cnt = 0
for stock in stocks:
    test=yf.Tickers(stock)
    for ticker in test.tickers:
        try:
            info = ticker.info
            results[stock] = info
        except:
            results[stock] = None
    cnt += 1
    if cnt%10 == 0:        
        print(cnt)


# In[24]:


import pandas as pd
import json
with open(r'C:\Users\chenxun2\hk2.json', 'w') as fp:
    json.dump(results, fp)
df = pd.read_json(r'C:\Users\chenxun2\hk2.json')
df1 = pd.DataFrame.transpose(df)
df1.head()
df1.to_excel(r'C:\Users\chenxun2\hk2.xlsx')


# In[ ]:




