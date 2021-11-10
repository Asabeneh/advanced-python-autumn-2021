from fetch_data import fetch_data
import json
from pprint import pprint

url = 'https://api.thecatapi.com/v1/breeds'
data =  fetch_data(url)

""" list_cat = []
for cat in data:
    life_span = cat['life_span'].split('-')
    lowest_age = int(life_span[0])
    heighest_age = int(life_span[1])
    age = (lowest_age + heighest_age) / 2
    list_cat.append([cat['origin'],cat['name'], age])
pprint(list_cat) """

with open('cats.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)