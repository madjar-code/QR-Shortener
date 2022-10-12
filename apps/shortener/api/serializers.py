from rest_framework.serializers import ModelSerializer

from shortener.models import Link, LinkTemplate


class LinkSerializer(ModelSerializer):
    class Meta:
        model = Link
        fields = ('long_url', 'short_url', 'status', 'session')


class LinkTemplateSerializer(ModelSerializer):
    class Meta:
        model = LinkTemplate
        fields = ('id', 'name', 'url')