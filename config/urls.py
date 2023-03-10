from rest_framework import permissions
from django.conf import settings
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from apps.shortener.api.routers import shortener_router


urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/', include('apps.shortener.api.urls')),
    path('api/', include('apps.files.api.urls'))
]

urlpatterns += shortener_router.urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

schema_view = get_schema_view(
   openapi.Info(
      title="QR-Shortener API",
      default_version='v1',
      description="API для взаимодействия с QR-сокращателем.",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="admin@admin.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns += [
   re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]