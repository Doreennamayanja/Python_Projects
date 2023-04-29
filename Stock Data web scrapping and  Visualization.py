#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import plotly.graph_objects as plt
import requests
import json
import os #operating system
apikey = os.environ.get("apikey") #to call api key save on the pc


# In[24]:


r = requests.get(f"https://financialmodelingprep.com/api/v3/historical-price-full/zm?timeseries=180&apikey={apikey}") #getting data from this website, zm is the stock symbol for zoom and 180 are the number of days to show on the graph
r = r.json()
historical = r["historical"] #historical is the dictionary
df = pd.DataFrame(historical)
df


# In[30]:


fig = go.Figure(data=[go.Candlestick(x=df['date'],open=df['open'],high=df['high'],low=df['low'],close=df['close'])]) #show the columns date, open, high, low, close.

fig.update_layout(title="Candlestick Chart for ",yaxis_title="Price")
fig.show()


# In[31]:


def candlestick(symbol,days):  #created a function candlestick and arguments symbol and days
    r = requests.get(f"https://financialmodelingprep.com/api/v3/historical-price-full/{symbol}?timeseries={days}&apikey={apikey}") #replace zm with symbol and 180 with days
    r = r.json()
    historical = r["historical"] #
    df = pd.DataFrame(historical)

    fig = go.Figure(data=[go.Candlestick(x=df['date'],open=df['open'],high=df['high'],low=df['low'],close=df['close'])]) #show the columns date, open, high, low, close.

    fig.update_layout(title="Candlestick Chart for "+ symbol,yaxis_title="Price") #include symbol in this line
    fig.show()    #using this function you can visualize any stocks for by specifying the stock symbol and days as shown in the next line


# In[33]:


candlestick("zm",180) #showing zoom stocks for 180 days


# In[35]:


candlestick("tsla",365) #showing tesla stocks for a year


# In[36]:


candlestick("msft",180) #stocks for Microsoft


# In[37]:


candlestick("amzn",180) #stocks for amazon for the past year


# In[ ]:




