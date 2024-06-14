from django.shortcuts import render, redirect
from django.contrib import messages
from firebase_admin import auth
from django.template import loader
from .forms import UserRegistrationForm, UserLoginForm
from django.http import HttpResponse
from .utils.firebase_utils import sign_in_with_email_and_password

from .decorators import firebase_auth_required


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
                user = auth.create_user(email=email, password=password)
                messages.success(request, 'User registered successfully.')
                return redirect('login')
            except Exception as e:
                messages.error(request, str(e))
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
                result = sign_in_with_email_and_password(email, password)
                if 'idToken' in result:
                    # messages.success(request, 'User logged in successfully.')
                    request.session['firebase_token'] = result['idToken']
                    return redirect('dashboard')
                else:
                    messages.error(request, result.get('error', {}).get('message', 'Login failed'))
            except Exception as e:
                messages.error(request, 'Login failed: {}'.format(e))
        else:
            messages.error(request, 'Invalid form data')
    else:
        form = UserLoginForm()

    return render(request, 'login.html', {'form': form})

@firebase_auth_required
def dashboard(request):
    template = loader.get_template('dashboard.html')
    return HttpResponse(template.render())

def logout(request):
    if 'firebase_token' in request.session:
        del request.session['firebase_token']
    return redirect('login')




