from django.shortcuts import render, get_object_or_404
from .models import Cafe
from .forms import RegisterForm, LoginForm

def index(request): 
    all_cafes = Cafe.objects.all()
    return render(request, 'index.html', {'all_cafes': all_cafes})

def get_cafe_info(request):
    all_cafes = Cafe.objects.all()
    cafe_id = request.GET.get('cafe_id')
    cafe = get_object_or_404(Cafe, id=cafe_id)
    return render(request, 'index.html', {'all_cafes': all_cafes, 'cafe': cafe})

def sign_in(request):
    form = LoginForm()
    return render(request, "login.html", {'form': form} )

def register(request):
    form = RegisterForm()
    return render(request, "register.html", {'form': form} )

def logout(request):
    pass