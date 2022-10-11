from rest_framework.serializers import ModelSerializer

from ..models import Link


class LinkSerializer(ModelSerializer):
    class Meta:
        model = Link
        fields = ('long_url', 'short_url', 'status', 'session')
