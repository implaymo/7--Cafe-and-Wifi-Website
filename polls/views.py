from django.shortcuts import render, get_object_or_404, redirect
from .models import Cafe
from .forms import RegisterForm, LoginForm, AddCafe
from django.contrib.auth import authenticate, login, logout



def index(request): 
    all_cafes = Cafe.objects.all()
    return render(request, 'index.html', {'all_cafes': all_cafes})

def get_cafe_info(request):
    """Makes all the cafe information show on the middle of the screen"""
    all_cafes = Cafe.objects.all()
    cafe_id = request.GET.get('cafe_id')
    cafe = get_object_or_404(Cafe, id=cafe_id)
    return render(request, 'index.html', {'all_cafes': all_cafes, 'cafe': cafe})

def sign_in(request):
    form = LoginForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("index")
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

def logout_view(request):
    logout(request)
    return redirect("index")

def add_new_cafe(request):
    form = AddCafe(request.POST)
    if request.method == "POST":
        if form.is_valid():
            name = form.cleaned_data["name"]
            map_url = form.cleaned_data["map_url"]
            img_url = form.cleaned_data["img_url"]
            location = form.cleaned_data["location"]
            seats = form.cleaned_data["seats"]
            has_toilet = form.cleaned_data["has_toilet"]
            has_wifi = form.cleaned_data["has_wifi"]
            has_sockets = form.cleaned_data["has_sockets"]
            can_take_calls = form.cleaned_data["can_take_calls"]
            coffee_price = form.cleaned_data["coffee_price"]
            
            cafe_instance = Cafe(
                name=name,
                map_url=map_url,
                img_url=img_url,
                location=location,
                seats=seats,
                has_toilet=has_toilet,
                has_wifi=has_wifi,
                has_sockets=has_sockets,
                can_take_calls=can_take_calls,
                coffee_price=coffee_price
            )
            cafe_instance.save()
            return redirect("index")
        else:
            error_message = "Something went wrong. Try again"
            return render(request, "add_cafe.html", {"form": form, "error_message": error_message})
    else:
        return render(request, "add_cafe.html", {"form": form})

