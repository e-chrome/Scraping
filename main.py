import requests
from bs4 import BeautifulSoup

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:2.0.1) Gecko/20100101 Firefox/4.0.1'
}

KEYWORDS = ['TypeScript', 'криминалист', 'помощник', 'IoT', 'релиз']
url = 'https://habr.com/ru/all/'
response = requests.get(url, headers=HEADERS)

soup = BeautifulSoup(response.text, 'html.parser')
articles = soup.find_all(name='article')
for article in articles:
    date = article.find_all('time')[0]['datetime'][:10]
    title = article.find_all(class_='tm-article-snippet__title-link')[0].find_all('span')[0].text
    link = 'https://habr.com' + article.find_all(class_='tm-article-snippet__title-link')[0]['href']
    text = ''
    list_text = article.find_all('p')
    for item in list_text:
        text += item.text
    for keyword in KEYWORDS:
        if title.find(keyword) != -1 or text.find(keyword) != -1:
            print(date + ' - ' + title + ' - ' + link)
            break





