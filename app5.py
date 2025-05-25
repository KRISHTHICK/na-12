import requests
from bs4 import BeautifulSoup

def fetch_trending_fashion():
    url = "https://www.examplefashionwebsite.com/trending"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    trends = []
    for item in soup.find_all('div', class_='trend-item'):
        trends.append(item.text)

    return trends
