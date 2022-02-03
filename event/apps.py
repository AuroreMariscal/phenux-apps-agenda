from django.apps import AppConfig


class EventConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.agenda.event' # Add name in INSTALLED_APPS in settings.py of core
