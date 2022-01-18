from django.shortcuts import render
from .models import Project


def home(request):
    projects = Project.objects.all()                                        # импорт всех записей из базы данных
    return render(request, 'portfolio/home.html', {'projects': projects})
