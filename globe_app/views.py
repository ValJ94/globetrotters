from django.shortcuts import render
from globe_app.models import *

def index(request):
    return render(request, 'globe_templates/index.html')





