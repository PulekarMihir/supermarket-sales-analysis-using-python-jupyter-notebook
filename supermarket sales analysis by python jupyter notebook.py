#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


sales = pd.read_csv(r"C:\Users\MIHIR\Desktop\Datasets\supermarket sales\supermarket_sales - Sheet1.csv")


# In[3]:


sales


# In[4]:


sales.head()


# In[5]:


sales.tail()


# In[6]:


sales.shape


# In[7]:


sales.size


# In[8]:


sales["Product line"]


# In[9]:


sales.info()


# In[10]:


sales.isnull().sum()


# In[11]:


sales.nunique()


# In[12]:


sales.describe()


# # 1 . which city has more females shopping
# 

# In[13]:


sales.groupby(['City','Gender']).count()


# In[18]:


female_shoppers = sales.groupby(['Gender','City']).count()['Customer type']


# In[19]:


print(female_shoppers)


# In[21]:


female_shoppers.unstack(level=0).plot(kind = 'bar')
plt.legend(loc='lower right')


# # 2. How spends more ? men or women

# In[22]:


sales.groupby('Gender').sum()


# In[23]:


spend = sales.groupby('Gender').sum()['Total']
spend.plot(kind = 'bar')


# # 3. Which type of customer spend more ? member or normal.

# In[24]:


sales.groupby('Customer type').sum()


# In[25]:


spend = sales.groupby('Customer type').sum()['Total']
spend.plot(kind = 'bar')


# # 4.Which product line sales more?
# 

# In[33]:


product_line = sales.groupby('Product line').count()['Invoice ID']


# In[34]:


print(product_line)


# In[35]:


product_line.plot(kind= 'bar')
plt.grid(axis = 'y')


# # 5. Which product line is popular among men vs. women ?

# In[37]:


sales.groupby(['Gender','Product line']).count()["Invoice ID"]
sales_gender = sales.groupby(['Gender','Product line']).count()["Invoice ID"]
sales_gender.unstack(level = 0).plot(kind = 'bar')
plt.legend(loc = 'lower right')
plt.grid(axis = 'y')


# # 6.What days of month make most sales?
# 7.What months makes most sales?

# In[38]:


sales['Date']


# In[39]:


pd.to_datetime(sales['Date'])


# In[40]:


pd.to_datetime(sales['Date']).dt.day
pd.to_datetime(sales['Date']).dt.month
sales['Day'] = pd.to_datetime(sales['Date']).dt.day
sales['Month'] = pd.to_datetime(sales['Date']).dt.month
sales.head(10)


# In[45]:


sales.groupby('Day').sum()['Total'].plot()
plt.grid()


# In[47]:


sales.groupby('Month').sum()['Total'].plot(kind = 'bar')
plt.grid(axis = 'y')


# # 8.What hours make most sales?

# In[48]:


sales['Time']


# In[50]:


pd.to_datetime(sales['Time'])


# In[51]:


sales['Hour'] = pd.to_datetime(sales['Time']).dt.hour
sales.head(10)


# In[52]:


sales.groupby('Hour').sum()['Total'].plot()
plt.grid()


# # 9. What time do people make more e-payment vs. What time do people make cash payment?

# In[53]:


sales.groupby(['Payment','Hour']).count()['Customer type']


# In[54]:


sales.groupby(['Payment','Hour']).count()['Customer type'].unstack(level=0).plot(kind = 'bar')
plt.grid(axis = 'y')
plt.legend(loc = 'lower right')


# # 10.Which city hast best rating?

# In[55]:


rating = sales.groupby('City').mean()['Rating']
rating.plot(kind = 'bar')
plt.grid(axis = 'y')


# In[ ]:




