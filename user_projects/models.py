from django.db import models
from django.contrib.auth.models import User
from platforms.models import ProgrammingLanguage, DatabaseType, Platform

class UserProject(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    backend_language = models.ForeignKey(ProgrammingLanguage, on_delete=models.SET_NULL, null=True, blank=True)
    database_type = models.ForeignKey(DatabaseType, on_delete=models.SET_NULL, null=True, blank=True)
    deployed_on_platform = models.ForeignKey(Platform, on_delete=models.SET_NULL, null=True, blank=True)
    deployment_url = models.URLField(blank=True)
    notes = models.TextField(blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
