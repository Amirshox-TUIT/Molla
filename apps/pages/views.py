from django.shortcuts import render

def home(request):
    return render(request, 'pages/home.html')

def about(request):
    return render(request, 'pages/about.html')

def contact(request):
    return render(request, 'pages/contact.html')

def faq(request):
    return render(request, 'pages/faq.html')

def coming_soon(request):
    return render(request, 'pages/coming-soon.html')

def error_404(request):
    return render(request, 'pages/404.html')
