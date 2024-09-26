from django.shortcuts import render

def brands_view(request):
    return render(request, 'brands/index.html')
