from django.contrib import admin
from .models import Platform, ProgrammingLanguage, DatabaseType, Feature

admin.site.register(Platform)
admin.site.register(ProgrammingLanguage)
admin.site.register(DatabaseType)
admin.site.register(Feature)
