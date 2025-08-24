from django.urls import path
from . import views

urlpatterns = [
    path('cart/', views.cart, name='cart'),
    path('category/', views.category, name='category'),
    path('checkout/', views.checkout, name='checkout'),
    path('product/', views.product_detail, name='product_detail'),
    path('wishlist/', views.wishlist, name='wishlist'),
]
