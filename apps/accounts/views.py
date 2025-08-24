from django.shortcuts import render

def dashboard(request):
    return render(request, 'auth/dashboard.html')

def login_view(request):
    return render(request, 'auth/login.html')
