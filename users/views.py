from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect 
from django.contrib import messages
from .forms import UserRegisterForm 


# Create your views here.

def index(request):
    return render(request, 'users/home.html', {})


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'User account created successfully.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

