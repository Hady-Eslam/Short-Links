from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _




class Url(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(_('Url Title'), max_length=100, default='')
    description = models.CharField(_('Url Description'), max_length=2000, default='')
    url = models.CharField(_('Url'), max_length=2000)
    short_url = models.CharField(_('Short Url'), max_length=100)
    is_deleted = models.BooleanField(_('Is Url Deleted'), default=False)
    created_at = models.DateTimeField(_('Url Created At'), auto_now_add=True)


    class Meta:
        indexes = [
            models.Index(fields=['short_url'], name='short_url_idx'),
            models.Index(fields=['short_url', 'is_deleted'], name='short_url_without_delete_idx')
        ]
