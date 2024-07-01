from django.shortcuts import render
from .models import Leadership
# Create your views here.

def index(request):
    return render(request, 'index.html')


def chronicle(request):
    return render(request, 'chronicle.html')

def politics(request):
    return render(request, 'politics.html')

def leader(request):
    leaders = Leadership.objects.all()
    return render(request, 'leader.html', {"leaders": leaders})

def leader_detail(request, pk):
    leader = Leadership.objects.get(id=pk)
    return render(request, 'leader_detail.html', {"leader": leader})

def product(request):
    return render(request, 'product.html')
