from rest_framework.serializers import ModelSerializer

from ..models import Link


class ShortenerSerializer(ModelSerializer):
    class Meta:
        model = Link
        fields = '__all__'
