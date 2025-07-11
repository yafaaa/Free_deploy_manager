from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserProjectViewSet, recommend_backend_language

router = DefaultRouter()
router.register(r'my-projects', UserProjectViewSet, basename='userproject')

urlpatterns = [
    path('', include(router.urls)),
    path('recommend/', recommend_backend_language, name='recommend-backend-language'),  # URL remains the same under projects
]
