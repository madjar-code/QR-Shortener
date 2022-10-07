from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from files.qr_generator import QRGenerator
from shortener.models import Link
from .serializers import FileSerializer
from .utils import shortening


@api_view(['POST'])
def shorten_links_from_excel(request):
    file_serializer = FileSerializer(data=request.data)

    if file_serializer.is_valid():
        excel_url = shortening(file_serializer)
        all_links = Link.objects.all()
        all_links.delete()
        return Response({'excel_url': excel_url})

    return Response(file_serializer.errors,
                    status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def make_an_archive(request):
    file_serializer = FileSerializer(data=request.data)

    if file_serializer.is_valid():
        excel_url = shortening(file_serializer)
        qr_generator = QRGenerator()
        qr_generator.generate_all_QR_codes()
        archive_url = qr_generator.archive_images_and_delete()
        all_links = Link.objects.all()
        all_links.delete()
        return Response({'excel_url': excel_url,
                         'archive_url': archive_url})

    return Response(file_serializer.errors,
                    status=status.HTTP_400_BAD_REQUEST)
