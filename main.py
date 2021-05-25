import requests
import csv

keyword = input('masukkan keyword : ')
pages = input('masukkan jumlah halaman (50 item/halaman) : ')
pages = int(pages)

write = csv.writer(open('hasil/{}.csv'.format(keyword), 'w', newline=''))
header = ['Brand', 'Nama', 'Harga', 'Diskon', 'Harga Sebelum Diskon']
write.writerow(header)

url = 'https://shopee.co.id/api/v4/search/search_items'

count = 0
for page in range(0,pages):
  parameter = {
    'by' : 'relevancy',
    'keyword' : keyword,
    'limit' : 50,
    'newest' : page,
    'order' : 'desc',
    'page_type' : 'search',
    'scenario' : 'PAGE_GLOBAL_SEARCH',
    'version' : 2,
  }

  r = requests.get(url, params=parameter).json()

  items = r['items']

  for p in items:
    brand = p['item_basic']['brand']
    name = p['item_basic']['name']
    price = p['item_basic']['price']
    discount = p['item_basic']['discount']
    price_before_discount = p['item_basic']['price_before_discount']
    count+=1
    print('No. ', count, 'brand : ',brand, 'name : ',name, 'price : ', price)

    write = csv.writer(open('hasil/{}.csv'.format(keyword), 'a', newline=''))
    data = [brand if brand else "Tidak Ada Merek", name if name else "N/A", price, discount if discount else "N/A", price_before_discount if price_before_discount else "N/A"]
    write.writerow(data)