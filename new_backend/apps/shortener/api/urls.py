from django.urls import path
from .views import create_short_url


urlpatterns = [
    path('long-url/', create_short_url)
]