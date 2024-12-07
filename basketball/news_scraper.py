import requests
from bs4 import BeautifulSoup

def fetch_basketball_news():
    url = 'https://www.srmist.edu.in/category/sports-achievements/'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    news_items = []

    # Modify this based on the actual HTML structure
    for article in soup.find_all('article', class_='type-post'):
        title = article.find('h2', class_='entry-title').text
        link = article.find('a')['href']
        description = article.find('div', class_='entry-summary').text.strip()
        
        # Check if the title or description mentions "basketball"
        if 'basketball' in title.lower() or 'basketball' in description.lower():
            news_items.append({
                'title': title,
                'link': link,
                'description': description
            })

    return news_items
