from urllib.request import urlretrieve
import requests

def get_book_list():
    url = "https://www.gutenberg.org/cache/epub/feeds/pg_catalog.csv"
    list_name = 'assets/gutenberg_book_list.csv'
    response = requests.get(url)
    with open(list_name, 'wb') as f:
        f.write(response.content)

def download_book(book_id, filename=''):
    
    pass

def title_helper(title):
    pass

def jaacard(a,b):
    A= set(a), B= set(b)
    if not A and not B:
        return 1.0
    if not A or not B:
        return 0.0 
    return len(A & B) / len(A | B)