from django.http import HttpResponse
from django.shortcuts import render
import os
from django.conf import settings

def home(request):
    # Render the index.html template from the templates directory
    return render(request, "index.html")
