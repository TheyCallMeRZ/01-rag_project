from urllib.request import urlretrieve
import requests

def get_book_list():
    url = "https://www.gutenberg.org/cache/epub/feeds/pg_catalog.csv"
    list_name = 'assets/gutenberg_book_list.txt'
    response = requests.get(url)
    with open(list_name, 'wb') as f:
        f.write(response.content)

get_book_list()
