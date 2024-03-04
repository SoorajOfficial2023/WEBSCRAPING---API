import requests
import json
import pandas as pd

with open('competitors_list.json', 'r') as file:
    competitors_list = json.load(file).get("competitors_list")

admart = pd.read_excel('admart.xlsx', sheet_name='Sheet1')
for i in range(0, len(admart)):
    for admart_name, admart_cat_list in zip(admart.loc[i]['name'], admart.loc[i]['categories']):
        search_term = admart_name.lower()
        for competitor in competitors_list:
            store_api = competitor.get('store_api')
            site = competitor.get('name')
            if store_api is not None:
                URL = store_api + search_term
                cookie = competitor.get('cookie')

                HEADERS = {
                    'Accept-Language': "en-US,en;q=0.9,hi;q=0.8",
                    'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36",
                    'Cookie': cookie
                }

                responces = requests.get(URL, headers=HEADERS)
                data = responces.json()
                items = data.get('items', [])

                
                if items:
                    df_items = pd.DataFrame(items)
                    cleaned_item = df_items[['name', 'base_price']]

                    for item in items:
                        categories = item.get('categories', [])
                        cat_names = [category.get('name', '') for category in categories]
                        print(cat_names)
                        # for cat_name in cat_names:
                        #     if cat_name.lower() in admart_cat_list.lower():
                        #         cleaned_item['category'] = cat_name
                        #         cleaned_item.to_excel(f"data2/{site}.xlsx", index=False)
                            # else:
                            #     print(None)
                else:
                    print(f"No items found for {admart_name} at {site}")

            else:
                print(f"Error: 'store_api' not found in competitor")
