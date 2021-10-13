import requests
import json
from fetch_api import fetch_api
url = 'https://api.thecatapi.com/v1/breeds'
data = fetch_api(url)
with open('cats.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

""" for cat in data:
    if 'image' in cat:
        img_url = cat['image']['url']
        img = requests.get(img_url).content
        name = cat["name"]
        with open(f'images/{name}.jpg', 'wb') as f:
            f.write(img) """

