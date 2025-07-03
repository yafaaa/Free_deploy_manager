from django.http import HttpResponse
from django.shortcuts import render
import os
from django.conf import settings

def home(request):
    # Serve the frontend/index.html file as the homepage
    frontend_path = os.path.join(settings.BASE_DIR, 'frontend', 'index.html')
    with open(frontend_path, encoding='utf-8') as f:
        return HttpResponse(f.read())
