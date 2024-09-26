from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),  # Главная страница
    path('shop/', include('shop.urls')),  # Магазин
    path('new/', include('new.urls')),  # Поступление
    path('brands/', include('brands.urls')),  # Партнёры
    path('about/', include('about.urls')),  # О нас
]
