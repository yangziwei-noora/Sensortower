#!/usr/bin/env python
# coding: utf-8

# In[3]:


from selenium import webdriver
import time
import urllib.request
from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
import sys


# In[5]:


link=["492",'19','21','4182','9','597','599','122','1756','4166','3859','3871','1742','4085','1664','4026']


# In[6]:


driver = webdriver.Chrome()
driver.get("https://store.steampowered.com/search/?filter=topsellers")
data=driver.page_source
soup = bs(data,"lxml")


# In[22]:


results= soup.find('div','page_content_ctn')


# In[28]:


tags=results.find_all('span', class_='tab_filter_control_label')
tgs=[]
for tag in tags:
    typenames=tag.string
    tgs.append(typenames)
    print(tgs)
    
tgs1=tgs[1:17]
tgs1


# In[46]:


tgs1[3]


# In[89]:


driver = webdriver.Chrome()
contents=[]
for i in link:
    driver.get("https://store.steampowered.com/search/?tags={}filter=topsellers".format(i))
    data=driver.page_source
    soupa=bs(data,'lxml')
    title=soupa.find_all("div",'col search_name ellipsis')
    time=soupa.find_all('div','responsive_search_name_combined')
    
    for t,m in zip(title,time):
        content={
            'appname':t.find('span','title').string,
            'publishtime':m.find('div','col search_released responsive_secondrow').string
        }
        contents.append(content)
        print(content)


# In[90]:


import pandas as pd
df=pd.DataFrame(contents)


# In[92]:


sms=list(tgs[1:17])
sms


# In[93]:


import numpy as np
n = 50
tggg=list(np.repeat(sms, n))
len(tggg)


# In[94]:


df["category"]=tggg


# In[100]:


lll=list(range(1,51))*16


# In[101]:


lll


# In[102]:


df['rank']=lll


# In[103]:


df


# In[105]:


df.to_csv('SteamTopCharts.csv', encoding='utf-8')


# In[ ]:




