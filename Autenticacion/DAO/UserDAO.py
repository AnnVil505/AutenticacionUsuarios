from django.shortcuts import get_object_or_404, render
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.db import IntegrityError

def signup(request):
    if request.method == 'GET':
        return render(request, 'create_user.html', {"form": UserCreationForm})
    else:

        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(
                    request.POST["username"], password=request.POST["password1"])
                user.save()
                login(request, user)
                return redirect('authentication')
            except IntegrityError:
                return render(request, 'create_user.html', {"form": UserCreationForm, "error": "Username already exists."})

        return render(request, 'create_user.html', {"form": UserCreationForm, "error": "Passwords did not match."})

def view_user(request):
    users = User.objects.all()
    return render(request, 'user.html', {"users": users})

def delete_user(request, user_name):
    user = get_object_or_404(User, username=user_name)
    if request.method == 'POST':
        user.delete()
        return redirect('user.html')
    
def create_user(request):
    return render(request, 'create_user.html')
