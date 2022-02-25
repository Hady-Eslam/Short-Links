from django.apps import AppConfig
from django.conf import settings
import os


class UrlConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    path = os.path.join(settings.BASE_DIR, 'Apps', 'Url')
    verbose_name = 'App For Urls'
    name = 'Apps.Url'
    label = 'Url'
