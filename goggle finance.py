#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup as bs
import requests
import time
import pandas as pd
import matplotlib.pyplot as plt

url = 'https://www.google.com/finance/markets/most-active?hl=en'

page = requests.get(url)

soup = bs(page.text, 'html.parser')

tables = soup.find(class_ = "Vd323d")


# In[2]:


tables


# In[3]:


Symbols =[]

table_index = tables.find_all(class_ = 'COaKTb')

for row in table_index[0:]:
    index = row.text
    Symbols.append(index)

Names = []
table_name = tables.find_all(class_ = 'ZvmM7')

for row2 in table_name[0:]:
    full_name = row2.text
    Names.append(full_name)
    
Prices = []
table_price = tables.find_all(class_ = 'YMlKec')

for row3 in table_price[0:]:
    stock_price = row3.text
    Prices.append(stock_price)
    
Changes = []
table_change = tables.select('.P2Luy.Ebnabc, .P2Luy.Ez2Ioe')

for row4 in table_change[0:]:
    price_change = row4.text
    Changes.append(price_change)
    
Per_Changes = []
table_per_change = tables.find_all(class_ = 'JwB6zf')

for row5 in table_per_change[0:]:
    stock_per_change = row5.text
    Per_Changes.append(stock_per_change)


# In[4]:


df = pd.DataFrame({'symbol': Symbols, 
                   'name': Names, 
                   'price($)': Prices, 
                   'change': Changes, 
                   '%_change': Per_Changes})
df


# In[5]:


df.info()


# In[6]:


# Clean the columns
df['price($)'] = df['price($)'].str.strip('$').astype(float)

df['change'] = df['change'].str.replace(r'\$', '', regex=True).astype(float)

df['%_change'] = df['%_change'].str.strip('%').astype(float)


# In[7]:


# 1. Heatmap for % Change
import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style="white")
plt.figure(figsize=(20, 12))

heatmap_data = df.pivot(index='price($)', columns='symbol', values='%_change')
sns.heatmap(heatmap_data, cmap='coolwarm', vmin=0, vmax=5)

plt.title('% Change Heatmap', fontdict={'fontsize': 30, 'fontweight': 'bold'}) # Set chart title size
plt.xlabel('Symbol', fontdict={'fontsize': 20, 'fontweight': 'bold'}) # Set x-axis label size and boldness
plt.ylabel('Price ($)', fontdict={'fontsize': 20, 'fontweight': 'bold'}) # Set y-axis label size and boldness
plt.xticks(fontsize=22) # Set x-axis tick size
plt.yticks(fontsize=15) # Set y-axis tick size
plt.tight_layout()
plt.show()


# In[19]:


# 2. Bar Chart for Market Cap (logarithmic scale)
sns.set(style="darkgrid") 
plt.figure(figsize=(15, 13))
ax = sns.barplot(x='change', y='symbol', data=df, palette='Blues_d') 
plt.xlabel('Symbol', fontdict={'fontsize': 20, 'fontweight': 'bold'}) # Set x-axis label size and boldness
plt.ylabel('Change', fontdict={'fontsize': 20, 'fontweight': 'bold'}) # Set y-axis label size and boldness
plt.xticks(fontsize=22) # Set x-axis tick size
plt.yticks(fontsize=16) # Set y-axis tick size
plt.title('Market Changes',  fontdict={'fontsize': 30, 'fontweight': 'bold'})
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()


# In[23]:


sns.set(style="darkgrid", font_scale=1.2)
plt.figure(figsize=(12, 6))
sns.scatterplot(x='price($)', y='change', data=df, hue='%_change', palette='coolwarm', alpha=0.8)
plt.xscale('log')
plt.xlabel('Price($)', fontdict={'fontsize': 16})  # Set x-axis label size
plt.ylabel('Change in price', fontdict={'fontsize': 16})  # Set y-axis label size
plt.title('Price($) vs Change in price (Colored by % Change)', fontdict={'fontsize': 20, 'fontweight': 'bold'})
plt.grid(True)
plt.tight_layout()
plt.show()


# In[24]:


# Data Storage
df.to_csv('stock_prices.csv', index=False)


# In[ ]:




