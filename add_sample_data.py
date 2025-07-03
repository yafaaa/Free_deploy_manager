from platforms.models import ProgrammingLanguage, DatabaseType, Feature, Platform

# Create or get programming language
python, _ = ProgrammingLanguage.objects.get_or_create(name='Python')

# Create or get database type
sqlite, _ = DatabaseType.objects.get_or_create(name='SQLite')

# Create or get features
rest_api, _ = Feature.objects.get_or_create(name='REST API', description='Support for RESTful APIs')

# Create or get a platform
platform, _ = Platform.objects.get_or_create(
    name='Example Platform',
    defaults={
        'description': 'A platform for deploying Python apps with SQLite and REST API support.',
        'url': 'https://example.com',
        'free_tier_description': 'Free tier with limited resources.',
        'supports_custom_domains': True,
        'has_auto_sleep': False,
        'notes': 'Demo platform for testing.'
    }
)

# Add relationships
platform.supported_languages.add(python)
platform.supported_databases.add(sqlite)
platform.supported_features.add(rest_api)

print('Sample data added!')
