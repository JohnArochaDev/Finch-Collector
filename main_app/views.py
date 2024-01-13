from django.shortcuts import render
from .models import Finch
# Create your views here.

def home(request):
    return render(request, 'home.html')

def about (request):
    return render(request, 'about.html')

def finch_index(request):
    finch = Finch.objects.all()
    return render(request, 'finch/index.html', {'finch' : finch })

def finch_detail(request, finch_id):
    finch = Finch.objects.get(id=finch_id)
    return render(request, 'finch/detail.html', {'finch' : finch})
