from django.shortcuts import render, get_object_or_404, redirect
from .models import Cafe
from .forms import RegisterForm, LoginForm
from django.contrib.auth import authenticate, login



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
    if request.method == "POST":
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                redirect("index")
            else:
                error_message = "Something was wrong. Try again"
                return render(request, "login.html", {'form': form, "error_message": error_message})
    return render(request, "login.html", {'form': form})

def register(request):
    form = RegisterForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            error_message = "Something went wrong. Try again"
            return render(request, "register.html", {'form': form, "error_message": error_message})
    else:
        return render(request, "register.html", {'form': form})

def logout(request):
    pass