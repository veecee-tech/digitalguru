from django.shortcuts import render
from .models import Service


def home(request):
    context ={
        'services' : Service.objects.all()
    }
    return render(request, 'index.html', context)