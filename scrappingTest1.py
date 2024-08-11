import requests
from bs4 import BeautifulSoup
import pandas as pd

#Getting the HTML
r = requests.get("").text
# print(r.text)

#Manipulating the data
soup = BeautifulSoup(r, "html.parser")

res = soup.find_all('div', class_="product")

products = {'title':[],'price':[],'url':[],'imageUrl':[],}

baseUrl = ''

for product in res:
    # name = product.find('figure').
    url = product.find('figure').a['href']
    imageUrl = product.find('figure').a.img['data-src']
    title = product.h3.a.string
    price = product.find('span',class_='product-price').string
    price = price.replace('$','')
    price = price.replace('.','')
    price = price
    # products.append({'title':title,'price':price,'url':f'{baseUrl}{url}', 'imageUrl':f'{imageUrl}'})
    products['title'].append(title)
    products['price'].append(int(price))
    products['url'].append(f'{baseUrl}{url}')
    products['imageUrl'].append(imageUrl)

print(products)

df = pd.DataFrame(products)
df.to_excel("products.xlsx", index=False)