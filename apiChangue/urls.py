from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from .CustomAuthToken import CustomAuthTokenAPI

schema_view = get_schema_view(
    openapi.Info(
        title="Sensores API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="detreaty@gmail.com"),
        license=openapi.License(name="BSD raulanto"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),

)

urlpatterns = [
    path('', lambda request: redirect('admin/', permanent=False)),
    path('admin/', admin.site.urls),
    path('api-token-auth/', CustomAuthTokenAPI.as_view()),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/', include('blog.api.urls')),

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
