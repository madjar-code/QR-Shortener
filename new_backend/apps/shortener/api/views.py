from rest_framework.decorators import api_view
from rest_framework.response import Response

from files.models import Session
from shortener.shortener import Shortener
from shortener.models import Link


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
    link.delete()
    return Response({
        'short url': short_url,
        'session id': session.id})
