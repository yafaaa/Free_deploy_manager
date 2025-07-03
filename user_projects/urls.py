from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserProjectViewSet

router = DefaultRouter()
router.register(r'my-projects', UserProjectViewSet, basename='userproject')

urlpatterns = [
    path('', include(router.urls)),
]
