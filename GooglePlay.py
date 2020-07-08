#!/usr/bin/env python
# coding: utf-8

# In[22]:


import requests
from bs4 import BeautifulSoup
headers={
  'user-agent':'Mozilla/5.0'
}
url='https://play.google.com/store/apps/top?hl=en_US'

html1=requests.get(url)
soup1=BeautifulSoup(html1.text,'html.parser')
link1=[]
for item in soup1.find_all('div','Z3lOXb'):
    link=item.find('div','W9yFB').find('a')['href']
    link1.append(i)


# In[1]:


url='https://play.google.com/store/apps/top?hl=en_US'
headers={
    'user-agent':'Mozilla/5.0'
}
page=1

import requests
from bs4 import BeautifulSoup
for n in range(1,2):
    html=requests.get(url+str(page),headers=headers)
    page+=1
    soup = BeautifulSoup(html.text,'html.parser')
    
    link1=[]
    for item in soup.find_all('div','Z3lOXb'):
        link=item.find('div','W9yFB').find('a')['href']
        link1.append(link)
        print(link)


# In[2]:


link1[0]


# In[5]:


A=link1[0]
B=link1[1]
C=link1[2]
D=link1[3]


from selenium import webdriver
import time
from bs4 import BeautifulSoup as bs

driver = webdriver.Chrome()
driver.get("https://play.google.com"+A)
data_a=driver.page_source
soup_a=bs(data_a,'lxml')
linka=[]
for item in soup_a.find_all('div','Vpfmgd'):
        link=item.find('div','vU6FJ p63iDd').find('a')['href']
        linka.append(link)
        print(linka)
        
driver = webdriver.Chrome()
driver.get("https://play.google.com"+B)
data_b=driver.page_source
soup_b=bs(data_b,'lxml')

linkb=[]
for item in soup_b.find_all('div','Vpfmgd'):
        link=item.find('div','vU6FJ p63iDd').find('a')['href']
        linkb.append(link)
        print(linkb)
        
driver = webdriver.Chrome()
driver.get("https://play.google.com"+C)
data_c=driver.page_source
soup_c=bs(data_c,'lxml')
print("我是4")
linkc=[]
for item in soup_c.find_all('div','Vpfmgd'):
        link=item.find('div','vU6FJ p63iDd').find('a')['href']
        linkc.append(link)
        print(linkc)
        
driver = webdriver.Chrome()
driver.get("https://play.google.com"+D)
data_d=driver.page_source
soup_d=bs(data_d,'lxml')
print("我是4")
linkd=[]
for item in soup_d.find_all('div','Vpfmgd'):
        link=item.find('div','vU6FJ p63iDd').find('a')['href']
        linkd.append(link)
        print(linkd)


# In[6]:


linka


# In[22]:


driver = webdriver.Chrome()
topchart_type="Top Free APPs"
content_free1=[]
for i in linka:
    driver.get("https://play.google.com"+i)
    data_a=driver.page_source
    soupa=bs(data_a,'lxml')
    content_free=[]
    kill=soupa.find_all("div",'oQ6oV')
    you=soupa.find_all('div','jdjqLd')
    heheda=soupa.findAll('div','K9wGie')
    for k,y,h in zip(kill,you,heheda):
        content_free={
            'appname':k.find('h1','AHFaub').find('span').string,
            'developer':y.find('div','qQKdcc').find('span',"T32cc UAO9ie").find('a').string,
            'Rating':h.find('div','BHMmbe').string,
            'top_chart_type':topchart_type   
          }
        content_free1.append(content_free)
        print(content_free)


# In[23]:


driver = webdriver.Chrome()
topchart_type1="Top Grossing APPs"
content_grossing1=[]
for i in linkb:
    driver.get("https://play.google.com"+i)
    data_a=driver.page_source
    soupa=bs(data_a,'lxml')
    kill=soupa.find_all("div",'oQ6oV')
    you=soupa.find_all('div','jdjqLd')
    heheda=soupa.find_all('div','K9wGie')
    for k,y,h in zip(kill,you,heheda):
        content_grossing={
            'appname':k.find('h1','AHFaub').find('span').string,
            'developer':y.find('div','qQKdcc').find('span',"T32cc UAO9ie").find('a').string,
            'Rating':h.find('div','BHMmbe').string,
            'top_chart_type':topchart_type1   
          }
        content_grossing1.append(content_grossing)
        print(content_grossing)


# In[30]:


driver = webdriver.Chrome()
topchart_type2="Top Free Games"
content_freegames1=[]
for i in linkc:
    driver.get("https://play.google.com"+i)
    data_a=driver.page_source
    soupa=bs(data_a,'lxml')
    kill=soupa.find_all("div",'oQ6oV')
    you=soupa.find_all('div','jdjqLd')
    heheda=soupa.find_all('div','K9wGie')
    for k,y,h in zip(kill,you,heheda):
        content_freegames={
            'appname':k.find('h1','AHFaub').find('span').string,
            'developer':y.find('div','qQKdcc').find('span',"T32cc UAO9ie").find('a').string,
            'Rating':h.find('div','BHMmbe').string,
            'top_chart_type':topchart_type2   
          }
        content_freegames1.append(content_freegames)
        print(content_freegames)


# In[25]:


driver = webdriver.Chrome()
topchart_type1="Top Grossing Games"

content_grossinggames1=[]
for i in linkd:
    driver.get("https://play.google.com"+i)
    data_a=driver.page_source
    soupa=bs(data_a,'lxml')
    kill=soupa.find_all("div",'oQ6oV')
    you=soupa.find_all('div','jdjqLd')
    heheda=soupa.find_all('div','K9wGie')
    for k,y,h,top_chart_type in zip(kill,you,heheda,topchart_type33):
        content_grossinggames={
            'appname':k.find('h1','AHFaub').find('span').string,
            'developer':y.find('div','qQKdcc').find('span',"T32cc UAO9ie").find('a').string,
            'Rating':h.find('div','BHMmbe').string,
            'top_chart_type':topchart_type1  
          }
        content_grossinggames1.append(content_grossinggames)
        print(content_grossinggames)


# In[26]:


s=list(range(1,51))
m=list(range(1,49))


# In[27]:


import pandas as pd
df1=pd.DataFrame(content_free1)
df1['rank']=s


# In[28]:


df2=pd.DataFrame(content_grossing1)
df2['rank']=s
df2


# In[31]:


df3=pd.DataFrame(content_freegames1)
df3['rank']=s
df3


# In[32]:


df4=pd.DataFrame(content_grossinggames1)
df4['rank']=m
df4


# In[34]:


import pandas as pd
from functools import reduce
data_frames = [df1, df2, df3, df4]
df_merged = reduce(lambda  left,right: pd.merge(left,right,
                                            how='outer'), data_frames)


# In[35]:


df_merged.to_csv('google_play1.csv', encoding='utf-8')


# In[ ]:




