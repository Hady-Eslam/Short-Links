from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import serializers
from .serializers import UrlSerializer
from .mixins import BaseUrlAPI
from ..models import Url
from ..helper import Random




class UrlsAPI(BaseUrlAPI, ListCreateAPIView):
    throttle_scope = 'urls', '100/min'
    serializer_class = UrlSerializer

    def get_queryset(self):
        return Url.objects.filter(user=self.request.user, is_deleted=False).order_by('-id')

    def perform_create(self, serializer: serializers.ModelSerializer):
        _Count = Url.objects.count()
        serializer.save(user=self.request.user, short_url=Random.create_random_token(_Count + 1, _Count + 3))


class UrlAPI(BaseUrlAPI, RetrieveUpdateDestroyAPIView):
    throttle_scope = 'url', '100/min'
    serializer_class = UrlSerializer
    lookup_url_kwarg = 'Url_id'

    def get_queryset(self):
        return Url.objects.filter(user=self.request.user, is_deleted=False)
    
    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.save()
