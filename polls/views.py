from django.shortcuts import render, get_object_or_404, redirect
from .models import Cafe
from .forms import RegisterForm, LoginForm, AddCafe, EditCafe
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
    if request.method == "POST":
        form = AddCafe(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
        else:
            error_message = "Something went wrong. Try again"
            return render(request, "add_cafe.html", {"form": form, "error_message": error_message})
    else:
        form = AddCafe()
        return render(request, "add_cafe.html", {"form": form})

def edit_cafe_selected(request):
    if request.method == 'POST':
        cafe_id = request.POST.get('cafe_id')
        cafe = get_object_or_404(Cafe, id=cafe_id)
        form = EditCafe(request.POST, instance=cafe)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        cafe_id = request.GET.get('cafe_id')
        cafe = get_object_or_404(Cafe, id=cafe_id)
        form = EditCafe(instance=cafe)
    
    return render(request, "edit_cafe.html", {"form": form, "cafe_id": cafe_id})
    
def delete_cafe(request):
    if request.GET.get('cafe_id'):
        cafe_id = request.GET.get('cafe_id')
        print(f"CAFE {cafe_id}")
        cafe = cafe = get_object_or_404(Cafe, id=cafe_id)
        cafe.delete()
        return redirect("index")
    else:
        cafe_id = request.POST.get('cafe_id')
        cafe = get_object_or_404(Cafe, id=cafe_id)
        cafe.delete()
        
    return render(request, "index.html", {"cafe_id": cafe_id})

    