from django.shortcuts import render

def cart(request):
    return render(request, 'products/cart.html')

def category(request):
    return render(request, 'products/category.html')

def checkout(request):
    return render(request, 'products/checkout.html')

def product_detail(request):
    return render(request, 'products/product-detail.html')

def wishlist(request):
    return render(request, 'products/wishlist.html')
