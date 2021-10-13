import requests
from fetch_api import fetch_api
url = 'https://api.thecatapi.com/v1/breeds'
data = fetch_api(url)

for cat in data:
    if 'image' in cat:
        img_url = cat['image']['url']
        img = requests.get(img_url).content
        name = cat["name"]
        with open(f'images/{name}.jpg', 'wb') as f:
            f.write(img)

