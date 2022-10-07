from django.urls import path
from .views import *

urlpatterns = [
    path('shortening/', shorten_links_from_excel, name='shortening'),
    path('make-an-archive/', make_an_archive, name='make-an-archive'),
]