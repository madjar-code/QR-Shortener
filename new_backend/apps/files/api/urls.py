from django.urls import path
from .views import *

urlpatterns = [
    path('start-shortening/', shorten_links_from_excel, name='start-shortening'),
    path('start-shortening-archiving/', shorten_and_create_QR, name='start-shortening-archiving'),
    path('archive/', getting_archive_by_session_id, name='archive'),
    path('excel/', getting_excel_by_session_id, name='excel'),
    path('shortened-links/', getting_shortened_links_by_session_id, name='shortened-links'),
    path('clear/', delete_all_records, name='delete'),
    
    # path('make-an-archive/', make_an_archive, name='make-an-archive'),
]