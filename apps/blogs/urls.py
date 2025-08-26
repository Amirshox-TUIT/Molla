from django.urls import path
from . import views

app_name = 'blogs'

urlpatterns = [
    path('list', views.blog_list, name='blog_list'),
    path('detail', views.blog_detail, name='blog_detail'),
]
