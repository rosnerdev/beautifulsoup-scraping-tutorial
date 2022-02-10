from bs4 import BeautifulSoup
from requests import get

request = get('https://books.toscrape.com/').text

soup = BeautifulSoup(request, 'lxml')

books = soup.find_all('li', {'class': 'col-xs-6 col-sm-4 col-md-3 col-lg-3'})

list = []

for book in books:
    name = book.find('h3').find('a')['title']
    list.append(name)

print(list)