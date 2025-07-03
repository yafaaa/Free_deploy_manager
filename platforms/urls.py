from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_root, name='api_root'),
    path('recommend/', views.get_recommendations, name='get_recommendations'),
    # path('platforms/', views.platform_list, name='platform_list'),
    # path('platforms/<int:pk>/', views.platform_detail, name='platform_detail'),
]
