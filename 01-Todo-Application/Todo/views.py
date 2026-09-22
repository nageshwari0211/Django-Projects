from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import TODO
from django.contrib.auth.decorators import login_required

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username') or request.POST.get('Fnm')
        email = request.POST.get('email')
        password = request.POST.get('password') or request.POST.get('pwd')
        if not username or not password:
            return render(request, 'signup.html', {'error': 'Fill all fields'})
        if User.objects.filter(username=username).exists():
            return render(request, 'signup.html', {'error': 'Username already undi'})
        User.objects.create_user(username=username, email=email, password=password)
        return redirect('/login/')
    return render(request, 'signup.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username') or request.POST.get('Fnm')
        password = request.POST.get('password') or request.POST.get('pwd')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('/todo/')
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password - malli signup chey'})
    return render(request, 'login.html')

@login_required(login_url='/login/')
def todo(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            TODO.objects.create(user=request.user, title=title)
        return redirect('/todo/')
    todos = TODO.objects.filter(user=request.user)
    return render(request, 'todo.html', {'todos': todos, 'user': request.user})

def logout_view(request):
    logout(request)
    return redirect('/login/')