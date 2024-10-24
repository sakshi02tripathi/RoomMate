from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import UserRegisterForm, UserInfoForm

def homepage(request):
    return render(request, 'users/homepage.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('user_info')  # Redirect to user info page after login
    return render(request, 'users/login.html')

def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()  # Save the user
            return redirect('login')  # Redirect to login page after signup
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})  # Ensure this line points to 'register.html'

def user_info_view(request):
    if request.method == 'POST':
        form = UserInfoForm(request.POST)
        if form.is_valid():
            # Save user information (you may want to save it in a model)
            # Here we just redirect to the dashboard page
            return redirect('dashboard')  # Change 'dashboard' to your actual valid view name
    else:
        form = UserInfoForm()

    return render(request, 'users/user_info.html', {'form': form})

def dashboard_view(request):
    # Placeholder for the dashboard view
    return render(request, 'users/dashboard.html')
