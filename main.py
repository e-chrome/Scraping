import requests
from bs4 import BeautifulSoup

KEYWORDS = ['TypeScript', 'криминалист', 'помощник', 'IoT']
url = 'https://habr.com/ru/all/'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
articles = soup.find_all(name='article')
for article in articles:
    date = article.find_all('time')[0]['datetime'][:10]
    title = article.find_all(class_='tm-article-snippet__title-link')[0].find_all('span')[0].text
    link = 'https://habr.com' + article.find_all(class_='tm-article-snippet__title-link')[0]['href']
    for keyword in KEYWORDS:
        if title.find(keyword) != -1:
            a = title.find(keyword)
            print(date + ' - ' + title + ' - ' + link)
            break





