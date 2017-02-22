from django.shortcuts import render

"""[summary] Definições das views do sistema

[description]
"""


def home(request):
    return render(request, 'home.html')


def contact(request):
    return render(request, 'contact.html')
