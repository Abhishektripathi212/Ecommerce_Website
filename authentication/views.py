from django.shortcuts import render, redirect
from .forms import LoginForm, SignUpForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


@login_required(login_url='authentication:login')
def index(request):
    return render(request, 'index.html')


def login_view(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():

            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('authentication:index')
            else:
                form.add_error('email', 'Email or password is not correct')

        else:
            print(form.errors)
            print("form is not valid")
    return render(request, 'authentication/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('authentication:login')


def signup_view(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        user = form.save()
        login(request, user)  # Log the user in after signing up
        return redirect('authentication:index')
    return render(request, 'authentication/signup.html', {'form': form})

