import requests
from bs4 import BeautifulSoup

def scrape_headline_demo(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    headline = soup.find_all('h2')
    
    for idx, headline in enumerate(headline, 1):
        print(f'{idx}: {headline.text.strip()}')

scrape_headline_demo('url')