from django.contrib import admin
from django.urls import path, include
from catalog.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('catalog/', include('catalog.urls')),
    path('blog/', include('blog.urls')),
]
