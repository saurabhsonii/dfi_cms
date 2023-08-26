from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import LoginForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# custom 404 view
def custom_404(request, exception):
    return render(request, '404/404.html', status=404)
    
# Create your views here.

@login_required(login_url='login')
def index(request):
    return render(request, "dashboard/index.html")


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                # Change this to your desired URL after login
                return redirect('home')
            else:
                messages.error(
                    request, 'Invalid email or password. Please try again.')
    else:
        form = LoginForm()

    return render(request, 'dashboard/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

