import requests
from bs4 import BeautifulSoup
from html.parser import HTMLParser


def trade_spider(max_pages):
    page = 1
    while page <= max_pages:
        url = "http://www.blendernation.com/page/" + str(page) + "/"
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, 'html.parser')
        for link in soup.findAll('a', {'itemprop': 'url'}):
            href = link.get('href')
            title = link.string
            # print(href)
            # print(title)
            # print()
            get_single_item_data(href)
        page += 1


def get_single_item_data(item_url):
    source_code = requests.get(item_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, 'html.parser')
    for item_name in soup.findAll('h1', {'class': 'post-title'}):
        print(item_name.string)

trade_spider(2)
