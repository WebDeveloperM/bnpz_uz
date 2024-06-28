from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')


def chronicle(request):
    return render(request, 'chronicle.html')

def politics(request):
    return render(request, 'politics.html')

def leader(request):
    return render(request, 'leader.html')
