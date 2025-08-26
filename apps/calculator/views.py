from django.shortcuts import render, redirect
from .models import CalculatorModel
from apps.calculator.forms import CalculatorForm


def calculate_page(request):
    if request.method == 'POST':
        form = CalculatorForm(request.POST)
        result = None
        if form.is_valid():
            instance = form.save(commit=False)
            first_num = instance.first_num
            second_num = instance.second_num
            amal = instance.amal

            if amal == '+':
                result = first_num + second_num
            elif amal == '-':
                result = first_num - second_num
            elif amal == '*':
                result = first_num * second_num
            elif amal == '/':
                result = first_num / second_num

            instance.result = result
            instance.save()
            return render(request, 'calculator/calculate.html', {'result': result})

    else:
        return render(request, 'calculator/calculate.html')


def history_page(request):
    history_data = CalculatorModel.objects.all()  # Barcha ma'lumotlarni oladi
    return render(request, 'calculator/history.html', {'history': history_data})




