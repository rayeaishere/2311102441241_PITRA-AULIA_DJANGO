from django.urls import path
from .views import list_outfit

urlpatterns = [
    path('', list_outfit, name='list_outfit')
]