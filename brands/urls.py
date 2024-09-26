from django.urls import path
from .views import brands_view

urlpatterns = [
    path('', brands_view, name='brands'),
]
