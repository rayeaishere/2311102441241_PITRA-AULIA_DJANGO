from rayadanaga.views import home, about
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from user.views import (
    CategoryListCreateView, CategoryDetailView, 
    OutfitListCreateView, OutfitDetailView,
    SavedOutfitListCreateView, SavedOutfitDetailView

)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/categories/', CategoryListCreateView.as_view(), name='category-list-create'),
    path('api/categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    path('api/outfits/', OutfitListCreateView.as_view(), name='outfit-list-create'),
    path('api/outfits/<int:pk>/', OutfitDetailView.as_view(), name='outfit-detail'),
    path('api/saved-outfits/', SavedOutfitListCreateView.as_view(), name='saved-outfit-list-create'),
    path('api/saved-outfits/<int:pk>/', SavedOutfitDetailView.as_view(), name='saved-outfit-detail'),
    path('', home, name="home"),
    path('about', about, name="about")
]
