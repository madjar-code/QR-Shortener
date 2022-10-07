from django.urls import path
from .views import create_short_url


urlpatterns = [
    path('long_url/', create_short_url)
]