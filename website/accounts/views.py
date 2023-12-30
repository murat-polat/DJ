from django.shortcuts import render,redirect
from . forms import CreateUserForm, LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import auth
from django.contrib.auth import login, logout, authenticate
import asyncio
from asgiref.sync import sync_to_async

@sync_to_async
def index(request):
    return render(request, 'index.html')

@sync_to_async
def register(request):
    form = CreateUserForm()
    
    if request.method=='POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    context = {"registerform": form}
    return render(request, 'register.html', context=context)




@sync_to_async
def login(request):
    form = LoginForm()
    if request.user.is_authenticated:
        return render(request, "dashboard.html", {})
    if request.method == 'POST':    
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            email  = request.POST.get('email')
            user = authenticate(request, username=username, password=password, email=email)
            if user is not None:
                auth.login(request,user)
                # message = messages.success(request, "You are now logged in")
                
                return redirect('dashboard')
    context = {"loginform": form}
      
    return render(request, 'login.html', context=context)
   
@sync_to_async
@login_required
def dashboard(request):
    return render(request, 'dashboard.html')


def logout(request):
        auth.logout(request)
        # messages.success(request,("You now logget out!"))
        return redirect('index')
