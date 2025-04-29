from django.shortcuts import render
from blog.views import fetch_articles
# Create your views here.
def homepage(request):
    articles = fetch_articles()
    return render(request, 'home/index.html', {'articles': articles})