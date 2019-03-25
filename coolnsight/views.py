from django.shortcuts import render
from django.http import HttpResponse
from django.views.static import serve
import os
from django.conf import settings

def home(request):
    return render(request, 'home.html')

def get_file(request, file_name):
    filepath = os.path.join(settings.BASE_DIR, '.well-known/acme-challenge', file_name)
    return serve(request, os.path.basename(filepath), os.path.dirname(filepath))