import requests
import pandas as pd

cookie = "_fbp=fb.1.1703117409592.1874850120; _gcl_au=1.1.2133621296.1703117410; _pin_unauth=dWlkPVpERTJNMkpqTVdRdE0yWmlOeTAwTXpBekxUa3lORGd0TkRFeU1UQXpaRFU1TjJVeg; ajs_anonymous_id=79b76b6c-c8b1-4799-8dd9-6854a67552e5; sa-user-id=s%253A0-bbc83143-d682-5d93-67eb-0fa7dc042134.IfkQ6%252F6yjnYRGIHkolhzjFPL2A3fdfwqGnqu%252FibuEKk; sa-user-id-v2=s%253Au8gxQ9aCXZNn6w-n3AQhNMqkgsE.u9mCAq78bbj%252BhKmVktGLBDNw0b9NvEsmsvpkGgr2%252BtA; sa-user-id-v3=s%253AAQAKIAN_u6NFIHbzEdVHMq-kVF0n4pzDkUUVDBM6BIoDo3vZEAEYAyDi242qBjABOgThLiiVQgSe-bJZ.fzhJPsb9AAQb%252FBbkEpw8xp9cI%252F5MG4H%252B78UiIobgNCE; _pin_unauth=dWlkPVpERTJNMkpqTVdRdE0yWmlOeTAwTXpBekxUa3lORGd0TkRFeU1UQXpaRFU1TjJVeg; __stripe_mid=1ab480e5-0d3e-4696-b005-e5f79dc4ec1db6b84a; ajs_anonymous_id=79b76b6c-c8b1-4799-8dd9-6854a67552e5; _derived_epik=dj0yJnU9d2tBT1Zvak9tREFrZlhwMlpONTFha0hWdlVETVlqMXMmbj1BX1E2N1BMNS1ackJfSWVSd0xyYmdRJm09MSZ0PUFBQUFBR1hCcnVZJnJtPTEmcnQ9QUFBQUFHWEJydVkmc3A9NQ; __cf_bm=DJksothZ9On.pK2fYgf.r3R4tT_D5rroAD_I.ZAjgdY-1708016530-1.0-AW1ZedsagzbECUmlSQcm+SnMn4SNkx0O3OYBjDuCmVqG2fdr3RCt4qGuh3Gdho+U274M5xy/9tFSVi22Jlcrb8c=; lux_uid=170801653522487111; AMCVS_68B620B35350F1650A490D45%40AdobeOrg=1; AMCV_68B620B35350F1650A490D45%40AdobeOrg=179643557%7CMCIDTS%7C19769%7CMCMID%7C27115570064732389264596109635854455933%7CMCAAMLH-1708621335%7C12%7CMCAAMB-1708621335%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1708023735s%7CNONE%7CvVersion%7C5.5.0%7CMCCIDH%7C0; wfmStoreId=16; at_check=true; wfm.tracking.sessionStart=1708016536787; kndctr_68B620B35350F1650A490D45_AdobeOrg_identity=CiYyNzExNTU3MDA2NDczMjM4OTI2NDU5NjEwOTYzNTg1NDQ1NTkzM1IRCJL81M3IMRgBKgRJTkQxMAPwAbGk4O3aMQ==; kndctr_68B620B35350F1650A490D45_AdobeOrg_cluster=ind1; inRedirectGoldPanAudience=1; __stripe_sid=0deff797-9163-47e1-8152-f7f7f8da29aa62fccf; s_gpv=Search%20Results:%20apple%20|%20Wegmans; wfm.tracking.s10=1; session-prd-weg=.eJwdjk1vgjAAQP9Lz8ZQRDa4MUhcOylKinxcCEINxVoZBdEu--8jO7zLu7z3A8rLwFQL3EslFFuBsmfDrZJMjsAdh2kxiinF77Ic71cmgQvYC7fnXc0jjlGiESQcO-tFwto8vRZ0bYrHWTh94SMbdYkRUqRzGuo9zZ9RcB1JIEThw7bYJc99GoucCk5obebdB885UkiedJHhS5UeedQdjYh6mmjPJP7M8zQeq3T738pMcUVdPzXpU-39ZermTCyFjyYLeSTjV5MmCt1E2ywfIa1n0iWQ6BqST2ONZ-9Q4y38bo5wDlS2CfwhFtLq32X3dT4ob8el3dq4QgZYgUmxoeQNcC3LMTZvhm39_gHEMGo-.GK_VLQ.Mc3DwZyQuOYBw6kSuD8v_A7PtJk; _uetsid=f8b577f0cc2311ee8953df8446c8759e; _uetvid=a5096560293b11ee91b999b6876af653; wfm.tracking.x2p=1; _dd_s=rum=0&expire=1708017456971; _derived_epik=dj0yJnU9bkhjRER2U3p3NndSN0xIM3lyV1g1OF8wZjRnVnRnNjAmbj1WcU5kYlhhYzU0VUlNZ1lITDR3Wl93Jm09MSZ0PUFBQUFBR1hPUTY0JnJtPTEmcnQ9QUFBQUFHWE9RNjQmc3A9NQ; mbox=PC#0a4453c0c86c48228bf5fc30128da3b6.41_0#1771261346|session#f7388cc6f4474238ac2524093757ecab#1708018419"

HEADERS = {

    'Accept-Language': "en-US,en;q=0.9,hi;q=0.8",
    'User-Agent' : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36",
    'Cookie': cookie    
}

admart = pd.read_excel('admart.xlsx')

for i in range(0,len(admart)):
    search_term = admart.loc[i]['name']
    URL = f"https://shop.wegmans.com/api/v2/store_products?limit=3&search_term={search_term}"
    responces = requests.get(URL,headers=HEADERS)
    data = responces.json()
    items = data.get('items')
    df_items = pd.DataFrame(items)
    cleaned_item = df_items[['name','base_price']]
    cleaned_item.to_excel(f'data2/{search_term}.xlsx',index=False)
    