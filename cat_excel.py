import requests
import pandas as pd
import json
from colorama import *

with open('stores.json', 'r') as file:
    competitors_list = json.load(file).get('competitors_list')

category_data = pd.DataFrame()

for competitor_info in competitors_list:
    competitor_name = competitor_info.get('name')
    cookie = competitor_info.get('cookie')
    cat_url = competitor_info.get('cat_url')

    HEADERS = {
        'Accept-Language': "en-US,en;q=0.9,hi;q=0.8",
        'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36",
        'Cookie': cookie
    }

    response = requests.get(cat_url, headers=HEADERS)
    data = response.json()
    items = data.get('items')

    
    competitor_categories = pd.DataFrame({'Competitor': [competitor_name] * len(items), 'Category': [item.get('name') for item in items]})
    
   
    category_data = pd.concat([category_data, competitor_categories], ignore_index=True)


category_data.to_excel('categories.xlsx', index=False)
