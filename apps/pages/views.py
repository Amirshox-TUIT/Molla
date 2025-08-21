from django.shortcuts import render

def home_pages(request):
    return render(request, 'home.html')

def about_pages(request):
    return render(request, 'about.html')

def second_pages(request):
    return render(request, 'blog-list.html')

def third_pages(request):
    return render(request, 'blog-detail.html')
