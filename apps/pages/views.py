from django.shortcuts import render, redirect
from django.contrib import messages
from apps.pages.forms import ContactForm
from apps.pages.models import AboutModel


def home(request):
    return render(request, 'pages/home.html')

def about(request):
    persons = AboutModel.objects.all()
    context = {'persons': persons}
    return render(request, 'pages/about.html', context)

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Ваше сообщение успешно отправлено!")
            return redirect("pages:contact")
        else:
            messages.error(request, "Исправьте ошибки в форме и попробуйте снова.")
    else:
        form = ContactForm()
    return render(request, "pages/contact.html", {"form": form})

def faq(request):
    return render(request, 'pages/faq.html')

def coming_soon(request):
    return render(request, 'pages/coming-soon.html')

def error_404(request):
    return render(request, 'pages/404.html')
