from django.shortcuts import render
from django.http import JsonResponse
from .models import Platform, ProgrammingLanguage, DatabaseType, Feature
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.

@csrf_exempt
def get_recommendations(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Only POST allowed'}, status=405)
    try:
        data = json.loads(request.body.decode('utf-8'))
        lang_name = data.get('lang')
        db_name = data.get('db')
        feature_names = data.get('feature', [])

        if not lang_name and not db_name and not feature_names:
            return JsonResponse({"error": "At least one of 'lang', 'db', or 'feature' must be provided."}, status=400)

        required_languages = ProgrammingLanguage.objects.filter(name=lang_name) if lang_name else ProgrammingLanguage.objects.none()
        required_databases = DatabaseType.objects.filter(name=db_name) if db_name else DatabaseType.objects.none()
        required_features = Feature.objects.filter(name__in=feature_names)

        queryset = Platform.objects.all()

        if required_languages.exists():
            queryset = queryset.filter(supported_languages__in=required_languages)

        if required_databases.exists():
            queryset = queryset.filter(supported_databases__in=required_databases)

        if required_features.exists():
            for feature in required_features:
                queryset = queryset.filter(supported_features=feature)
        
        queryset = queryset.distinct()

        recommendations = []
        for platform in queryset:
            score = 0
            matched_langs = platform.supported_languages.filter(pk__in=required_languages.values_list('pk', flat=True)).count()
            matched_dbs = platform.supported_databases.filter(pk__in=required_databases.values_list('pk', flat=True)).count()
            matched_features = platform.supported_features.filter(pk__in=required_features.values_list('pk', flat=True)).count()

            score += matched_langs * 5
            score += matched_dbs * 5
            score += matched_features * 10

            if platform.has_auto_sleep:
                score -= 3

            matched_details = {
                'matched_languages': list(platform.supported_languages.filter(pk__in=required_languages.values_list('pk', flat=True)).values_list('name', flat=True)),
                'matched_databases': list(platform.supported_databases.filter(pk__in=required_databases.values_list('pk', flat=True)).values_list('name', flat=True)),
                'matched_features': list(platform.supported_features.filter(pk__in=required_features.values_list('pk', flat=True)).values_list('name', flat=True)),
            }

            recommendations.append({
                'id': platform.id,
                'name': platform.name,
                'description': platform.description,
                'url': platform.url,
                'free_tier_description': platform.free_tier_description,
                'score': score,
                'supports_custom_domains': platform.supports_custom_domains,
                'has_auto_sleep': platform.has_auto_sleep,
                'matched_details': matched_details,
            })

        recommendations.sort(key=lambda x: x['score'], reverse=True)

        return JsonResponse({'recommendations': recommendations})

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

def api_root(request):
    return JsonResponse({'message': 'Welcome to the API root.'})
