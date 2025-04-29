from django.urls import path
from .views import list_outfit
from . import views

urlpatterns = [
    path('', list_outfit, name='catalog_list'),
]