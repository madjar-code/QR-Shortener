from django.db.models import Q
from asgiref.sync import sync_to_async
from rest_framework.decorators import api_view
from rest_framework.response import Response
from shortener.shortener import Shortener
from shortener.models import Link
from shortener.api.serializers import LinkSerializer
from files.models import Session
from files.excel_handler import ExcelHandler
from files.qr_generator import QRGenerator
from .serializers import SessionSerializer, SimpleSessionSerializer


@api_view(['GET'])
def all_sessions():
    sessions = Session.objects.all()
    sessions_serializer =\
        SimpleSessionSerializer(sessions, many=True)
    return Response(sessions_serializer.data)


@api_view(['POST'])
def session(request):
    session_id = request.data['session_id']
    if session_id:
        try:
            session_instance = Session.objects.get(id=session_id)
        except Exception:
            return Response({'error': 'incorrect session id'})
        session_serializer = SessionSerializer(session_instance)
        return Response(session_serializer.data)
    return Response({'error': 'no session id'})


@sync_to_async
@api_view(['POST'])
def shorten_links_from_excel(request):
    if not request.data['input_file']:
        return Response({'error': 'no file'})
    session_serializer = SessionSerializer(data=request.data)
    if session_serializer.is_valid():
        session_serializer.save()
        session_instance = Session.objects.last()
        excel_handler = ExcelHandler(
            session=session_instance
        )
        excel_handler.create_records()
        shortener = Shortener()
        shortener.shorten_all_links()
        message = f'Session with ID = {session_instance.id}'
        return Response({'message': message})
    return Response({'error': 'Incorrect data'})


@api_view(['POST'])
def shorten_and_create_QR(request):
    if not request.data['input_file']:
        return Response({'error': 'no file'})
    session_serializer = SessionSerializer(data=request.data)
    if session_serializer.is_valid():
        session_serializer.save()
        session_instance = Session.objects.last()
        excel_handler = ExcelHandler(
            session=session_instance
        )
        excel_handler.create_records()
        shortener = Shortener()
        shortener.shorten_all_links()
        qr_generator = QRGenerator(
            session=session_instance
        )
        qr_generator.generate_all_QR_codes()
        qr_generator.archive_images_and_delete()
        message = f'Session with ID = {session_instance.id}'
        return Response({'message': message})
    return Response({'error': 'Incorrect data'})


@api_view(['POST'])
def getting_excel_by_session_id(request):
    session_id = request.data['session_id']
    if session_id:
        try:
            session_instance = Session.objects.get(id=session_id)
        except Exception:
            return Response({'error': 'incorrect session id'})
        shortened_links = Link.objects.filter(
            Q(session=session_instance, status=Link.STATUS_SHORTER) |
            Q(session=session_instance, status=Link.STATUS_READY))
        number_of_cut = len(shortened_links)
        number_of_all = len(Link.objects.filter(session=session_instance))
        excel_handler = ExcelHandler(
            session=session_instance
        )
        if number_of_all == number_of_cut:
            excel_url = excel_handler.create_result_excel()
            return Response({'excel_url': excel_url})    
        return Response({'excel_url': 'Not everything is ready yet'})
    return Response({'error': 'no session id'})


@api_view(['POST'])
def getting_archive_by_session_id(request):
    session_id = request.data['session_id']
    if session_id:
        try:
            session_instance = Session.objects.get(id=session_id)
        except Exception:
            return Response({'error': 'incorrect session id'})
        number_of_archive = len(Link.objects.filter(
            session=session_instance,
            status=Link.STATUS_READY))
        number_of_all = len(Link.objects.filter(session=session_instance))
        qr_generator = QRGenerator(
            session=session_instance
        )
        if number_of_all == number_of_archive:
            archive_url = qr_generator.archive_images_and_delete()
            return Response({'archive_url': archive_url})    
        return Response({'archive_url': 'Not everything is ready yet'})
    return Response({'error': 'no session id'})


@api_view(['POST'])
def getting_shortened_links_by_session_id(request):
    session_id = request.data['session_id']
    if session_id:
        try:
            session_instance = Session.objects.get(id=session_id)
        except Exception:
            return Response({'error': 'incorrect session id'})
        links = Link.objects.filter(session=session_instance)
        links_serializer = LinkSerializer(links, many=True)
        return Response(links_serializer.data)
    return Response({'error': 'no session id'})


@api_view(['DELETE'])
def delete_all_records(request):
    Link.objects.all().delete()
    Session.objects.all().delete()
    return Response({'message': 'Successful removal'})


@api_view(['DELETE'])
def delete_session(request):
    session_id = request.data['session_id']
    if session_id:
        try:
            session_instance = Session.objects.get(id=session_id)
        except Exception:
            return Response({'error': 'incorrect session id'})
        session_instance.delete()
        return Response({'message': 'success'})
    return Response({'error': 'no session id'})