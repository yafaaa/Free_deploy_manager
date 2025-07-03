from django.db import models

class ProgrammingLanguage(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class DatabaseType(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Feature(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Platform(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    url = models.URLField()
    free_tier_description = models.TextField()
    supports_custom_domains = models.BooleanField(default=False)
    has_auto_sleep = models.BooleanField(default=False)
    notes = models.TextField(blank=True)

    # Free tier limits (simplified for now)
    free_ram_mb = models.IntegerField(null=True, blank=True)
    free_disk_gb = models.IntegerField(null=True, blank=True)
    free_bandwidth_gb = models.IntegerField(null=True, blank=True)

    # Many-to-many relationships
    supported_languages = models.ManyToManyField(ProgrammingLanguage, related_name='platforms')
    supported_databases = models.ManyToManyField(DatabaseType, related_name='platforms')
    supported_features = models.ManyToManyField(Feature, related_name='platforms')

    def __str__(self):
        return self.name
