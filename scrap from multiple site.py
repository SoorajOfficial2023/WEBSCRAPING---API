import requests
import pandas as pd

competitior_list = [
    { 'url':"https://shop.sprouts.com/api/v2/store_products?ads_enabled=true&ads_pagination_improvements=true&allow_autocorrect=true&limit=10&offset=0&search_provider=ic&search_term=",
      'cookie':"_gcl_au=1.1.1424297023.1706679651; BVBRANDID=eb4c9c2f-fba4-4d90-b189-2e2520394ba9; _fbp=fb.1.1706679652900.436061966; _pin_unauth=dWlkPU9UZzNNalkzTldNdFptTTVOeTAwT0RFNExXSXlOREl0TVdRellUZzBORFJrWWpkaQ; ajs_anonymous_id=e8417584-9713-4714-b18a-279e2743b38d; _pin_unauth=dWlkPU9UZzNNalkzTldNdFptTTVOeTAwT0RFNExXSXlOREl0TVdRellUZzBORFJrWWpkaQ; ajs_anonymous_id=e8417584-9713-4714-b18a-279e2743b38d; __stripe_mid=db57c2b9-0eaa-4894-b6be-b1db9441dbd9b9a41c; _gid=GA1.2.1020739123.1707030354; loyaltyID=undefined; BVBRANDSID=ee0c4eef-da86-46df-be95-dc85f8577daa; __cf_bm=FwZacvK4eH.WxpH2shA3S3zbyvk51ibw.oH5K1ARIRo-1707115041-1-AbzAiE0/Cg1rCKDYMkUuVEcToV4JKlnHcfeM6iIWJfsQEP4ohQBBxh3jrAAQCSrkcqI0GmeIFrWG4w9uBc2tjI8=; _gat_UA-47434162-1=1; dotcomSearchId=d87b3902-5f2e-42ca-b6cc-a6d446be156c; __stripe_sid=0e5bc725-b236-4b46-9ce2-fa334ec92b054c5a28; session-sprouts=.eJwdjk1zgjAARP9Lzo5DAKVwc2RKw0CoFglwYRCChC8pCSI4_e-lPezl7c7se4GkGCgvgVGkDacbkPR0aNOOdgIYYhhXwinn7N4l4l7TDhiAznZ5tTLmMRtdFgQxs_XtCmEmB_OaJZObx7XR-_iI9qg6KZ4Z7TAJGsePW7eKBLYQdGdYun69OL4r4QrBv01s3iCeEUddsMShXaTkxLwKSXg5PD0zUzCbWETOIiW7_69QbmpU9WNOntw5rlKtPlICH3noMq87zzm5cNQ2Zb56uH424SpSPD-C-EPa6qmMcusreB-1BX4SJVSHy1okx3ty0IRQp1v_LbG-VYIJbMDI6ZCwHBiyqknwTdP2P7_d5Gkn.GKIUJw.3lucO35cOj9VjtFlMECsgbOe70A; _ga=GA1.2.786857746.1706679652; _uetsid=d7a33e80c32b11ee8a609dcb0827a1fd; _uetvid=4c00fe70bffb11eeaac0d9a26a92ee02; _ga_LPZ816BHL5=GS1.1.1707115039.8.1.1707115176.38.0.0; _dd_s=rum=0&expire=1707116076702"
    
    },
    {
      'url':"https://shop.wegmans.com/api/v2/store_products?ads_enabled=true&ads_pagination_improvements=true&allow_autocorrect=true&limit=5&offset=0&search_provider=ic&search_term=",
      'cookie':"_fbp=fb.1.1706678089289.1157664646; _pin_unauth=dWlkPU9UZzNNalkzTldNdFptTTVOeTAwT0RFNExXSXlOREl0TVdRellUZzBORFJrWWpkaQ; _gcl_au=1.1.1957802561.1706678090; ajs_anonymous_id=ec61c7d2-e364-4fbf-9428-4361a9aa8922; kndctr_68B620B35350F1650A490D45_AdobeOrg_identity=CiY3NDA5NjA4NjM5MTQ1NDUwMDM0MjM5NjM2NTczMTIxMTYwMDE3NlIRCKvqw-_VMRgBKgRJTkQxMAPwAa7hi5fXMQ==; wfmStoreId=16; inRedirectGoldPanAudience=1; _pin_unauth=dWlkPU9UZzNNalkzTldNdFptTTVOeTAwT0RFNExXSXlOREl0TVdRellUZzBORFJrWWpkaQ; sa-user-id=s%253A0-c88b6d71-12ee-5be9-6d62-8a0037ae9ed1.SAc0Qq49QH4KYk5Jzr89BgAsRaPpE0VrZuNj76SWiPg; sa-user-id-v2=s%253AyIttcRLuW-ltYooAN66e0WeSr7Y.EBWj4QgVNysm%252BU3Mkj2ChBKBcbbBnhBfFimFaH7GWXw; sa-user-id-v3=s%253AAQAKIEzGg7GP0kKYguN0OqBzUJtNvAWBlQkLCaCLP6jC9s7iEAEYAyC0nsWrBjABOgTssIJHQgR2Wsof.XY43sPMCXzZTVM7ZfIBmv7PZWuDUDMm0SCPQuA5kRRw; __stripe_mid=29bddb83-f2fe-4373-90a2-76f1bbe1bcc4f55ba9; ajs_anonymous_id=ec61c7d2-e364-4fbf-9428-4361a9aa8922; kndctr_68B620B35350F1650A490D45_AdobeOrg_cluster=ind1; wfm.tracking.sessionStart=1707115301263; __cf_bm=5h1ZZsaHFrc1HsADhyBfamfBEqG6op0QuiqgQbRrycQ-1707115301-1-AUwes8OdJfIrjuL00sS2X0lD76+9CfhGWhi9LfKVRcFLepv3sk2+RCNmlTco/k4VF+nUM74EniEvRbzGsg9PcUY=; at_check=true; AMCVS_68B620B35350F1650A490D45%40AdobeOrg=1; AMCV_68B620B35350F1650A490D45%40AdobeOrg=179643557%7CMCIDTS%7C19758%7CMCMID%7C74096086391454500342396365731211600176%7CMCAAMLH-1707720103%7C12%7CMCAAMB-1707720103%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1707122503s%7CNONE%7CMCSYNCSOP%7C411-19761%7CMCCIDH%7C0%7CvVersion%7C5.5.0; dotcomSearchId=d601802e-6a44-4680-86f3-a53a72e39f18; lux_uid=170711531135213222; wfm.tracking.x2p=1; at_check=true; __stripe_sid=d9799583-12f4-41d6-9703-cf8da47241f33f1fbc; s_gpv=Search%20Results:%20apple%20|%20Wegmans; _uetsid=d5251fb0c32911ee858ec13c8f63d80a; _uetvid=a89f28e0bff711ee857c396da4869645; session-prd-weg=.eJwdjslugzAABf_F56iKWdLCrQI1MYpxkpIYc0EETDGLgzBLoOq_l_bwLnN4M98gzjuuCmDnSa34BsQt75pEctkDu--GlSiulHjIuH9UXAIb8Nkr7vtUEOGh64KgLzzrZYUw1W7zuiXV6vFeW23koB1qznoUfEG2XJpj4BV4Qb3vIhh9QsHKQvyxKCgqHKTQL_Hiz0gheVui0MsTehakPG9JgLfEZZrvTILRS59Q898VanWFynbI6FMdnTWqsQZO4ZiFWBB5mTN6Vaipi2ztWP8nv2Q6cd9NfNi-PJwJV2pvsPZETpmrQfMQj-NMkdS1-DlZ7Z6_fqg8NBEDGzAo3sUiA7ZhWLrxttsZP79mK2nL.GKIUvQ.urRaEKUfNEbUyuzKXoB2YT_81WM; _dd_s=rum=0&expire=1707116226018; mbox=session#8ed73dcb94474452a58866f50e0da94f#1707117187|PC#8ed73dcb94474452a58866f50e0da94f.41_0#1770360115"
    },
    {
      'url':"https://shop.thefreshmarket.com/api/v2/store_products?ads_enabled=true&ads_pagination_improvements=true&limit=60&offset=0&page=1&prophetScorer=frequency&sort=rank&allow_autocorrect=true&search_is_autocomplete=false&search_provider=ic&search_term=",
      'cookie':"osano_consentmanager_uuid=307c376c-f10d-4107-a573-c7e1f10af7f3; osano_consentmanager=3x8MgIHnK_nVJk5KmuOnd2sHDJYR8FP6k1pCkCaxdqC0pkZknRQR80VRjB6Kbgp7iGjMUnsPLnme8DWmUxRLBTj48Z3TkM1LJINdRgM__wpe-q8XngljF-JbFVnkfXq4LfhXRd5iPf89ikmPWXa635YOVLE924Ot8lU-D_E4Xy6P1mJcughXVg5oPt56dUVNqJH39oco4BAJ-E9jqf6qFimUuhbedA890lkIoINBn4wilHtXcqRTKzrDKkkaBU4EXcSmTg2iAG1Ry3jlpaURHTclVU9KceLsUfw0QQ==; _gcl_au=1.1.1454964145.1706631619; _gid=GA1.2.921200125.1706631621; _fbp=fb.1.1706631621548.1772768121; _pin_unauth=dWlkPU5qZzVOR1ZsTlRVdFl6SmtZeTAwWmpNekxUazBaVGd0TURoa01EWmxabVF4TkRNMg; ajs_anonymous_id=d6854b93-7b07-407f-a94f-839dc66712ed; __stripe_mid=6a035359-a082-4788-a444-cbc813a5b8ab5862e9; fw_se={%22value%22:%22fws2.904b7ea3-3c52-4b73-982f-fe0d1a5c7217.3.1706678484364%22%2C%22createTime%22:%222024-01-31T05:21:24.364Z%22}; _uetsid=76a87b70bf8b11eeb2461f63bc1d7a0c; _uetvid=76a8e760bf8b11ee8e7067f8c6f9fc7b; fw_chid={%22value%22:%22N7A4N3b%22%2C%22createTime%22:%222024-01-31T05:22:41.980Z%22}; _ga_EMDXDP2N4W=GS1.2.1706678486.2.1.1706678564.44.0.0; __stripe_sid=4de0f57b-def4-4649-9359-d819c0aac2c083aadd; __cf_bm=yKgtT0SxPcrWLh9iLS4z.5LN74Bl9gGS1bQ5nIlm1ws-1706679642-1-AQnN0qxyxZkNsf4EPffEx3ZkrpN7ENQJY2c8Qjwrw0X6fvsHxqE/74zELvOt4w5Uu5QgZKDHPi0k7f6cNWRKCUA=; session-prd-tfm=.eJxNic2OgjAYAN-lZ2MoWn-4bRTYNlJCFmTphQAW_VBAKaxSs---HPcwmWTmjdKyk-qCrDK7KTlD6V12ddbIpkdW3w1TUVIpaJu0b6-yQRaSI7vkbgE-MBppijmw7XyKuDCP44QuzNtPftvexY6uaFUsRWUbSegZh_BK_LDoucsgAQxJ5dSHONA89ha8nry3lwKoos1Ri29WZnEAfhWNXEcm197ysGMX4eJ7_v_XBOfuU9HaGXKTkDze4mKkq9Mnw-LrCVnsGLRqX1x_mLzyXn5o4zKYZxs_OLfQqeZJyt3eJqPI-qhU6WN9TgY4JnYPxoMzx1VohgYluxROyCLmmqzWi83vHyX9aTc.GJtu-A.RJLQ3Mfh0E7W1nhZBpran31K4Yg; _gat_UA-000000000-1=1; _dd_s=rum=0&expire=1706680572827; fw_utm={%22value%22:%22{}%22%2C%22createTime%22:%222024-01-31T05:41:13.278Z%22}; fw_uid={%22value%22:%2226a02601-620e-4807-af18-cc8bd1ab86fd%22%2C%22createTime%22:%222024-01-31T05:41:13.294Z%22}; _ga=GA1.1.1783481186.1706631620; _ga_2NZ40CS25B=GS1.1.1706678485.4.1.1706679673.57.0.0"
    }   
]

cookie = competitior_list[2]['cookie']
search_item = 'Apple'

HEADERS = {

    'Accept-Language': "en-US,en;q=0.9,hi;q=0.8",
    'User-Agent' : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36",
    'Cookie': cookie    
}

URL = competitior_list[2]['url']+'apple'
responces = requests.get(URL,headers = HEADERS)
data = responces.json()
items = data.get('items')
for item in items:
        print(item.get('name'))
        
print('---------filtered----------')

for item in items:
    for category in item.get('categories'):
      print(category.get('name'))

        # if (category.get('name')=='Fresh Fruits' or 'Fruits'):
        #     if (search_item in item.get('name')):
        #         print(item.get('name'))
        
    