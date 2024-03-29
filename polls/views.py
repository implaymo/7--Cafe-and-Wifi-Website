from django.shortcuts import render
from .models import Cafe


def index(request): 
    all_cafes = Cafe.objects.all()
    return render(request, 'index.html', {'all_cafes': all_cafes})
