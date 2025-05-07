from django.contrib import admin
from django.urls import path, include
from catalog.views import home
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('catalog/', include('catalog.urls')),
    path('blog/', include('blog.urls')),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
]

if settings.DEBUG:
    if settings.STATICFILES_DIRS:
        urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
    else:
        urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)