from rest_framework.viewsets import ModelViewSet
from shortener.api.serializers import LinkTemplateSerializer
from shortener.models import LinkTemplate


class LinkTemplateViewSet(ModelViewSet):
    serializer_class = LinkTemplateSerializer
    queryset = LinkTemplate.objects.all()
