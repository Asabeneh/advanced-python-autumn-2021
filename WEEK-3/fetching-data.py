import requests
import matplotlib.pyplot as plt
from pprint import pprint
from fetch_api import fetch_api
from wordcloud import WordCloud

url = 'https://api.thecatapi.com/v1/breeds'
data = fetch_api(url)

extracted_data = []
for cat in data:
    wt_metric_unit = cat['weight']['metric'].split()
    lowest_wt = int(wt_metric_unit[0])
    highest_wt = int(wt_metric_unit[2])
    average_wt = (lowest_wt + highest_wt) / 2
    life_span = cat["life_span"].split()
    life_span_lowest = int(life_span[0])
    life_span_highest = int(life_span[2])
    average_life_span = (life_span_lowest + life_span_highest) / 2
    extracted_data.append({
        'name':cat['name'],
        'weight':average_wt,
        'life_span':average_life_span
    })
# pprint(extracted_data)

sorted_cat = sorted(extracted_data, key = lambda x:x['weight'], reverse=True)[:10]

names = [item['name'] for item in sorted_cat]
weights = [item['weight'] for item in sorted_cat]

""" plt.bar(names, weights)
plt.xlabel('Names')
plt.ylabel('Weight in Kg')
plt.title('Cats Name and their weight')
plt.tight_layout(pad=0)
plt.savefig('cats_weight.png')
plt.show() """

stop_words = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were',
              'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]


import re


text = ''
for cat in data:
    text = text + cat['description']

cleaned_text = re.sub(r'[^a-zA-Z ]', ' ', text.lower())
words = cleaned_text.split()
words = [word for word in words if word not in stop_words]
# pprint(words)

freq_table = {}
for word in words:
    if word in freq_table:
        freq_table[word] = freq_table[word] + 1
    else:
        freq_table[word] = 1


sorted_dict = {k:v for k, v in sorted(freq_table.items(), key=lambda item: item[1], reverse=True)}
print(sorted_dict)

wordcloud = WordCloud().generate(' '.join(words))
plt.imshow(wordcloud, interpolation='bilinear')
plt.figure()
plt.axis("off")
plt.show()




