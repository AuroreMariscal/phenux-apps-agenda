from django.apps import AppConfig


class AgendaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.agenda.plugins' # Add name in INSTALLED_APPS in settings.py of core
