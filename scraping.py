import requests
import pandas as pd

cookie = "1.1.1424297023.1706679651; BVBRANDID=eb4c9c2f-fba4-4d90-b189-2e2520394ba9; _fbp=fb.1.1706679652900.436061966; _pin_unauth=dWlkPU9UZzNNalkzTldNdFptTTVOeTAwT0RFNExXSXlOREl0TVdRellUZzBORFJrWWpkaQ; ajs_anonymous_id=e8417584-9713-4714-b18a-279e2743b38d; _pin_unauth=dWlkPU9UZzNNalkzTldNdFptTTVOeTAwT0RFNExXSXlOREl0TVdRellUZzBORFJrWWpkaQ; ajs_anonymous_id=e8417584-9713-4714-b18a-279e2743b38d; __stripe_mid=db57c2b9-0eaa-4894-b6be-b1db9441dbd9b9a41c; _gid=GA1.2.1020739123.1707030354; BVBRANDSID=88cec317-721b-41fc-99c8-14a8e32b99ea; loyaltyID=undefined; __cf_bm=1K4prZ9crPiyDIn4gTFJvm5TmGlhX6TGGk703Q_m53Q-1707030356-1-ARhEzBKvChynGYz6CK8BkPcs4SFWp9+m3DXkztSIDLJTs2e9r60svU/zaquSQNgE1tCTWAsffLbBCNO268OfJxM=; dotcomSearchId=35bdba46-547d-4a11-a687-3e218ad0e8d0; __stripe_sid=3f4b106b-09c4-43f1-8bd8-b2b255499c882d823f; session-sprouts=.eJwdjsuOgjAAAP-lZ2MoKgg3V1y3RIoPtMKFQKmhUJBQEKnZf1-yh7nMZeYD4kfLZA7sRyIkm4G4YW2V1KzugN21_WQkk5I_67h7lqwGNmCjm6d7yn3uoqtCEHPXmk8SUv02Tiiqi1cqrCbaIgMV58pToRY5O-1ATgqrssOOy_EF5lHglgeyW4YVGqMgr7CzW3kXJFF9U9HdfSTkxP0CaVht3r5DF5gPPCTnLiGr_9ZdFyUqmj4jb3nYTlOV1TMCX9nd4359HjNylagSeTZ9eAEdcBEu_CCE-Eebcxo4gmqebqaxTFeO0YzfR2vYf5n0eO03T2NvDnC7zpDYgBnoJWtjngFbX5oaXJum8fsHS2dpMw.GKDJGQ.arPD96L4SHt-4tQOQP_9jhtwsX4; _ga_LPZ816BHL5=GS1.1.1707030354.6.1.1707030425.58.0.0; _ga=GA1.2.786857746.1706679652; _gat_UA-47434162-1=1; _uetsid=d7a33e80c32b11ee8a609dcb0827a1fd; _uetvid=4c00fe70bffb11eeaac0d9a26a92ee02; _dd_s=rum=1&id=8a94b380-c36a-4db9-8c29-c0f82608bc70&created=1707030405072&expire=1707031326220"
HEADERS = {

    'Accept-Language': "en-US,en;q=0.9,hi;q=0.8",
    'User-Agent' : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36",
    'Cookie': cookie    
}

admart_df = pd.read_excel("admart.xlsx",sheet_name="Sheet1")

for i in range(0,len(admart_df)):
    search_term = admart_df.loc[i]['name']
    URL = f"https://shop.sprouts.com/api/v2/store_products?ads_enabled=true&ads_pagination_improvements=true&allow_autocorrect=true&limit=5&offset=0&search_provider=ic&search_term={search_term}&secondary_results=true&sort=rank&unified_search_shadow_test_enabled=false"
    responces = requests.get(URL,headers = HEADERS)
    data = responces.json()
    items = data['items']
    df_items = pd.DataFrame(items)
    cleaned_items = df_items[['name','base_price']]
    cleaned_items.to_excel(f"data/{search_term}.xlsx",index=False)    
    
