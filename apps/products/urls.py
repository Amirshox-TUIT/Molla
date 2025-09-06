from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('cart/', views.cart, name='cart'),
    path('', views.products_view, name='products'),
    path('checkout/', views.checkout, name='checkout'),
    path('detail/', views.product_detail, name='detail'),
    path('wishlist/', views.wishlist, name='wishlist'),
]
