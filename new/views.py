from django.shortcuts import render

def new_view(request):
    return render(request, 'new/index.html')
