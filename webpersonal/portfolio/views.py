from django.shortcuts import render
from .models import Project, models

# Create your views here.

def portfolio(request):
    projects = Project.objects.all()
    return render(request, "portfolio/portfolio.html",{'projects':projects})