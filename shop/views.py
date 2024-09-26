from django.shortcuts import render
from django.shortcuts import render

def shop_view(request):
    return render(request, 'shop/index.html',)

