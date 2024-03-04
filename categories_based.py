import requests
import pandas as pd
import json
from colorama import*

with open('stores.json','r')as file:
    competitors_list = json.load(file).get('competitors_list')
    
search_item = input('enter the item: ')
search_item = search_item.lower()

for competitor in competitors_list:
    print(Style.BRIGHT+Fore.RED+competitor.get('name'))
    cookie = competitor.get('cookie')
    HEADERS = {

            'Accept-Language': "en-US,en;q=0.9,hi;q=0.8",
            'User-Agent' : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36",
            'Cookie': cookie    
        }
    URL = competitor.get('store')+search_item
    responces = requests.get(URL,headers=HEADERS)
    data = responces.json()
    items = data.get('items')
    

    for item in items:
        if (search_item in item.get('name').lower()):
            print(Style.BRIGHT+Fore.BLUE+item.get('name'))
            for category in item.get('categories'):
                print(Style.BRIGHT+Fore.CYAN+category.get("name"))
            print("-----------------------")