from rest_framework.decorators import api_view
from rest_framework.response import Response

from files.models import Session
from shortener.shortener import Shortener
from shortener.models import Link, LinkTemplate
from .serializers import LinkTemplateSerializer


@api_view(['POST'])
def create_short_url(request):
    long_url = request.data['long_url']
    session = Session.objects.create()
    link = Link.objects.create(
        long_url=long_url,
        session=session
    )
    Shortener().shorten_one_link(link)
    short_url = link.get_short_url()
    return Response({
        'short url': short_url,
        'session id': session.id})


@api_view(['GET'])
def all_templates(request):
    templates = LinkTemplate.objects.all()
    templates_serializer = LinkTemplateSerializer(templates, many=True)
    return Response(templates_serializer.data)