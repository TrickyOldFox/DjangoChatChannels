from django.shortcuts import render
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
from django.contrib import auth
from django.shortcuts import redirect
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        f = CustomUserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request, 'Account created successfully')
            return redirect('accounts_login')
 
    else:
        f = CustomUserCreationForm()
 
    return render(request, 'registration/register.html', {'form': f})

def login(request):
    if request.user.is_authenticated:
        return redirect('home')
 
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
 
        if user is not None:
            # correct username and password login the user
            auth.login(request, user)
            return redirect('home')
 
        else:
            messages.error(request, 'Error wrong username/password')
 
    return render(request, 'registration/login.html')
 
 
def logout(request):
    auth.logout(request)
    return render(request,'registration/logout.html')
 

def home(request):
    if not request.user.is_authenticated:
        return redirect('accounts_login')
 
    return render(request, 'registration/home.html')