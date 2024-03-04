import requests
import pandas as pd
import json
from colorama import*

with open('stores.json','r')as file:
    competitors_list = json.load(file).get('competitors_list')
    
for competitor in competitors_list:
    print(Style.BRIGHT+Fore.RED+competitor.get('name'))
    cookie = competitor.get('cookie')
    HEADERS = {

            'Accept-Language': "en-US,en;q=0.9,hi;q=0.8",
            'User-Agent' : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36",
            'Cookie': cookie    
        }
    URL = competitor.get('cat_url')
    responces = requests.get(URL,headers=HEADERS)
    data = responces.json()
    items = data.get('items')
    
    for category in items:
        print(Style.BRIGHT+Fore.CYAN+category.get("name"))
        print("-----------------------")