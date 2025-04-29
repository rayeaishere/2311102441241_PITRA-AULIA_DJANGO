from django.urls import path
from . import views
from .views import blog_list

urlpatterns = [
    path('', views.blog_list, name = 'blog_list'),
    path('articles/', blog_list, name='blog_articles'),
]