from django.urls import path

from apps.calculator.views import calculate_page, history_page

app_name = 'calculator'


urlpatterns = [
    path('calculate/', calculate_page, name='calculate'),
    path('history/', history_page, name='history'),
]