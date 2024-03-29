from django.shortcuts import render
from .models import Cafe


def index(request): 
    return render(request, 'index.html')

def get_all_cafes(request):
    all_map_urls = Cafe.objects.values_list('map_url', flat=True)
    return render(request, 'cafe_list.html', {'all_map_urls': all_map_urls})