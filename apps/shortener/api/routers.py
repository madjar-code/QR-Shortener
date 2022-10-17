from rest_framework.routers import DefaultRouter
from .viewsets import *


shortener_router = DefaultRouter()

shortener_router.register(
    'api/link-templates', 
    LinkTemplateViewSet, 
    basename='LinkTemplateViewSet')
