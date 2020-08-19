from selenium import webdriver
import time
import urllib.request
from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
import sys



driver = webdriver.Chrome()
tag = sys.argv[1]
url = 'https://sensortower.com/ios/rankings/top/iphone/us/games/{}?date=2020-06-23'.format(tag)
driver.get(url)

data=driver.page_source
soup = bs(data,"lxml")

results= soup.find(class_='rankings-app-body')
results1= soup.find(class_='shadowed-st flex-header slim flex-span-8 title-section')
        
a=results1.find_all('span',{"class":'rankings-title-extra'})

for i in a:
    b=i.get_text().split('-')[3]
    print(b)
types=str(b)

pricetype=("Free","Paid","Top Grossing")
pricetype1=list(pricetype)*50
len(pricetype1)
# https://sensortower.com/ios/rankings/top/iphone/us/games/action?date=2020-06-23
out=[]
 
names1=results.find_all('a', class_='name')
prices1=results.find_all('a',class_='price')
for name1,price1,pricetype in zip(names1,prices1,pricetype1):
    data={
        'name':name1.get_text(),
        'price':price1.get_text(),
        'type':types,
        'pricetype':pricetype
    }
    out.append(data)
    print(out)

df=pd.DataFrame(out)

df['index_column']=df.index
df['rank'] = df.groupby("pricetype")["index_column"].rank()
del df['index_column']

path = sys.argv[2]
df.to_csv('{}.csv'.format(path), encoding='utf-8')