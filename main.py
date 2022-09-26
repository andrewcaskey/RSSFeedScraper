import requests
from bs4 import BeautifulSoup

url = "https://lifehacker.com/rss"
resp = requests.get(url)
soup = BeautifulSoup(resp.content, features="xml")

# will find all item tags and give content in each tag
# of
items = soup.findAll('item')
len(items)
item = items[0]
# print(item)

# print item title
print(item.title.text)
# print url of content

#
news_items = []
for item in items:
    news_item = {}
    news_item['title'] = item.title.text
    news_item['description'] = item.description.text
    #news_item['link'] = item.link.text
    news_items.append(news_item)

print(news_items)
print(news_items[4])