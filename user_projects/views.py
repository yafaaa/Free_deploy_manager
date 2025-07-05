from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.decorators import parser_classes
from .models import UserProject
from .serializers import UserProjectSerializer
from .permissions import IsOwner
from django.http import JsonResponse
import json

class UserProjectViewSet(viewsets.ModelViewSet):
    queryset = UserProject.objects.all()
    serializer_class = UserProjectSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        # Ensure users can only access their own projects
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Automatically associate the logged-in user with the project
        serializer.save(user=self.request.user)

@csrf_exempt
def recommend_backend_language(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'POST required'}, status=405)
    try:
        body = json.loads(request.body.decode('utf-8') or '{}')
    except json.JSONDecodeError:
        body = {}
    print('DEBUG BODY PARSED:', body)
    lang = body.get('lang')
    db = body.get('db')
    traffic = body.get('expected_traffic')
    size = body.get('data_size')

    combos = [
        {'name': 'JavaScript + PostgreSQL','description': 'Vercel Hobby & Supabase Free','traffic': ['tiny','hobby'],'size':['small']},
        {'name': 'Python + PostgreSQL','description': 'Render Free Web Service & Neon Free','traffic': ['tiny','hobby'],'size':['small']},
        {'name': 'Go + MySQL','description': 'Fly.io Free & PlanetScale Dev','traffic': ['tiny','hobby','busy'],'size':['small','medium','large']},
        {'name': 'Java + MongoDB','description': 'AWS Free (EC2/Lambda) & MongoDB Atlas Free','traffic': ['tiny','hobby','busy'],'size':['small']},
        {'name': 'PHP + MySQL','description': 'Google Cloud Run Free & PlanetScale Dev','traffic': ['tiny','hobby','busy'],'size':['small','medium','large']},
    ]

    matches = []
    for combo in combos:
        combo_lang, combo_db = combo['name'].split(' + ')
        if combo_lang == lang and combo_db == db and traffic in combo['traffic'] and size in combo['size']:
            matches.append({'name': combo['name'], 'description': combo['description']})
    if not matches:
        matches = [{'name': c['name'], 'description': c['description']} for c in combos]

    received = {'lang': lang, 'db': db, 'expected_traffic': traffic, 'data_size': size}
    return JsonResponse({'received': received, 'recommendations': matches})
