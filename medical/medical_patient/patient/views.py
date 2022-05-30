from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import PatientForm


def menu(request):
    return render(request, 'patients/menu.html', {'title': 'Главная'})


def create(request):
    useform = PatientForm()
    return render(request, 'patients/create.html', {"form": useform, 'title': 'Новый пациент'})


def information(request):
    inf = Patient.objects.all()
    return render(request, 'patients/information.html', {'inf': inf, 'title': 'Информация о пациенте'})


def search(request):
    return render(request, 'patients/search.html', {'title': 'Поиск пациента'})

