from django.urls import path
from . import views

app_name = 'blogs'

urlpatterns = [
    path('', views.blog_list, name='list'),
    path('detail/<int:pk>/', views.blog_detail, name='detail'),
]
