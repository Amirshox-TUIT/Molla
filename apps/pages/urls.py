from django.urls import path

from apps.pages.views import about_pages, home_pages, second_pages, third_pages

app_name = 'pages'

urlpatterns = [
    path('about/', about_pages, name='about'),
    path('', home_pages, name='home'),
    path('2/', second_pages, name='two'),
    path('3/', third_pages, name='three'),
]