from django.urls import path
from .views import new_view

urlpatterns = [
    path('', new_view, name='new'),
]
