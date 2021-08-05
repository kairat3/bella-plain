from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from product.views import ProductApiView

router = DefaultRouter()
router.register('products', ProductApiView)

urlpatterns = [
    path('', include('account.urls')),
    path('', include('product.urls')),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('', include('info.urls')),
    path('', include('news.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
