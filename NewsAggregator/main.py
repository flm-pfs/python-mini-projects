import requests
from bs4 import BeautifulSoup
import datetime


class NewsAggregator:
    def __init__(self, sources):
        self.sources = sources

    def fetch_news(self, source):
        try:
            response = requests.get(source['url'])
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            articles = soup.find_all(
                source['article_tag'], class_=source['article_class'])
            news = []
            for article in articles:
                title = article.find(
                    source['title_tag'], class_=source['title_class']).get_text()
                link = article.find(
                    source['link_tag'], class_=source['link_class'])['href']
                news.append({'title': title, 'link': link})
            return news
        except requests.exceptions.RequestException as e:
            print(f"Error fetching news from {source['name']}: {e}")
            return []

    def get_all_news(self):
        all_news = []
        for source in self.sources:
            news = self.fetch_news(source)
            all_news.extend(news)
        return all_news

    def display_news(self, news):
        for item in news:
            print(f"Title: {item['title']}")
            print(f"Link: {item['link']}")
            print('-' * 80)


if __name__ == "__main__":
    # Define the sources of news
    sources = [
        {
            'name': 'BBC',
            'url': 'https://www.bbc.com/news',
                    'article_tag': 'div',
                    'article_class': 'gs-c-promo',
                    'title_tag': 'h3',
                    'title_class': 'gs-c-promo-heading__title',
                    'link_tag': 'a',
                    'link_class': 'gs-c-promo-heading'
        },
        {
            'name': 'CNN',
            'url': 'https://www.cnn.com',
                    'article_tag': 'article',
                    'article_class': 'cd__content',
                    'title_tag': 'h3',
                    'title_class': 'cd__headline-text',
                    'link_tag': 'a',
                    'link_class': 'cd__headline-text'
        }
    ]

    # Create an instance of the NewsAggregator class
    aggregator = NewsAggregator(sources)

    # Fetch all news from the sources
    news = aggregator.get_all_news()

    # Display the news
    aggregator.display_news(news)
