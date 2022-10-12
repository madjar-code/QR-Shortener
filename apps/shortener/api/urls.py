from django.urls import path
from .views import create_short_url, all_templates


urlpatterns = [
    path('long-url/', create_short_url, name='long-url'),
    path('templates/', all_templates, name='templates'),
]