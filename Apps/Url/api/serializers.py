from rest_framework import serializers
from rest_framework.reverse import reverse
from ..models import Url


class UrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = Url
        fields = ['title', 'description', 'url', 'short_url']
        extra_kwargs = {'short_url': {'read_only': True}}
    
    def to_representation(self, instance):
        instance.short_url = reverse(
            'Url:Redirect', kwargs={'Short_Url': instance.short_url}, request=self.context['request']
        )
        return super().to_representation(instance)
