import requests
import csv

key = input('masukkan keyword : ')
write = csv.writer(open('hasil/{}.csv'.format(key), 'w', newline=''))
header = ['Brand', 'Nama', 'Harga', 'Diskon', 'Harga Sebelum Diskon']
write.writerow(header)


url2 = 'https://api.bukalapak.com/multistrategy-products'
url1 = 'https://api.bukalapak.com/category-suggestions/categories'
url = 'https://shopee.co.id/api/v4/search/search_items'

parameter1 ={
  'term' : 'sepatu',
  'limit' : 3,
  'access_token' : 'pyot8mg1tmsmhmO36sr-rWhjMMLhrfxNisBjAWOUverbvQ'
}

count = 0
for page in range(0,2):
  parameter = {
    'by' : 'relevancy',
    'keyword' : key,
    'limit' : 50,
    'newest' : page,
    'order' : 'desc',
    'page_type' : 'search',
    'scenario' : 'PAGE_GLOBAL_SEARCH',
    'version' : 2,
  }

  r = requests.get(url, params=parameter).json()

  products = r['items']

  for p in products:
    brand = p['item_basic']['brand']
    name = p['item_basic']['name']
    price = p['item_basic']['price']
    discount = p['item_basic']['discount']
    price_before_discount = p['item_basic']['price_before_discount']
    count+=1
    print('No. ', count, 'brand : ',brand, 'name : ',name, 'price : ', price)

    write = csv.writer(open('hasil/{}.csv'.format(key), 'a', newline=''))
    data = [brand, name, price, discount, price_before_discount]
    write.writerow(data)