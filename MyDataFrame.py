#!/usr/bin/env python
# coding: utf-8

# In[35]:


import pandas as pd


# In[36]:


Mydataframe=pd.read_csv("Показатели продаж товарной группы.csv", delimiter=",")


# In[37]:


print(Mydataframe)


# In[38]:


print(Mydataframe.describe())


# In[39]:


print(Mydataframe.info())

