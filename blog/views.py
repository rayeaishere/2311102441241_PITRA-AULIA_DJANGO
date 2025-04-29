import requests
from django.shortcuts import render

API_KEY = '1fa3d195718d47738f63adf9941b5fc3'

def fetch_articles():
    url = (
        f'https://newsapi.org/v2/everything?'
        f'q=fashion&'
        f'language=en&'
        f'sortBy=publishedAt&'
        f'apiKey={API_KEY}'
    )
    
    try:
        response = requests.get(url)
        data = response.json()
        if data.get('status') == 'ok':
            return [
                {
                    'title': article['title'],
                    'summary': article['description'],
                    'url': article['url'],
                    'urlToImage': article.get('urlToImage'),
                }
                for article in data.get('articles', [])
                if article.get('title') and article.get('description')
            ]
    except Exception as e:
        print(f"Error: {e}")
    
    return []

def blog_list(request):
    articles = fetch_articles()
    return render(request, 'blog/blog_list.html', {'articles': articles})
