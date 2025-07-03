from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import UserProject
from .serializers import UserProjectSerializer
from .permissions import IsOwner

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
