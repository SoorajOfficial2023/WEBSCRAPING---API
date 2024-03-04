import pandas as pd
import numpy as np 
import json
from colorama import *
import requests

with open('stores.json','r')as file:
    competitors_list = json.load(file).get('competitors_list')
    
row_data = {}

for competitor in competitors_list:
    row_data.update({competitor.get('name'):[]})
    
for competitor in competitors_list:
    print(Fore.GREEN+"Fetching data from"+competitor.get('name'))
    URL = competitor.get('cat_url')
    cookie = competitor.get('cookie')
    HEADERS = {
        'Accept-Language': "en-US,en;q=0.9,hi;q=0.8",
        'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36",
        'Cookie': cookie
    }
    try:
        responses = requests.get(URL, headers=HEADERS)
        if responses.status_code == 200:
            data = responses.json()
            items = data.get('items')
            for item in items:
                row_data[competitor.get('name')].append(item.get('name'))
            print(Fore.GREEN+'category data fetched\n')
        else:
            print('not fetched')
            
    except:
        ValueError
max_length = max(len(a) for a in row_data.values())

for key,value in row_data.items():
    if len(value) < max_length:
        row_data[key] = value + [np.nan]* (max_length - len(value))
print(row_data)
df = pd.DataFrame(row_data)
df.to_excel('output/category.xlsx',index=False)



    
    