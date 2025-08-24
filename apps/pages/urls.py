from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('faq/', views.faq, name='faq'),
    path('coming-soon/', views.coming_soon, name='coming_soon'),
    path('404/', views.error_404, name='error_404'),
]
