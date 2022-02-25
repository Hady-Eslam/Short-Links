from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.apps import apps
import os


class LocalStorage(FileSystemStorage):

    def __init__(self) -> None:
        super().__init__(os.path.join(apps.get_app_config('Profile').path, 'media'))


def default_storage():
    return LocalStorage() if settings.DEBUG else LocalStorage()
