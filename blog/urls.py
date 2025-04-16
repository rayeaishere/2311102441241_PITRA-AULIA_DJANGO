from django.urls import path
from .views import get_fashion_articles

urlpatterns = [
    path('articles/', get_fashion_articles, name='get_articles'),
]