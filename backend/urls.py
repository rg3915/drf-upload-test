from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('api/v1/', include('backend.core.urls', namespace='core')),  # noqa E501
    path('admin/', admin.site.urls),
]

# djoser
urlpatterns += [
    path('api/v1/', include('djoser.urls')),
    path('api/v1/auth/', include('djoser.urls.authtoken')),
]

# swagger
urlpatterns += [
   path('swagger', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),  # noqa E501
   path('redoc', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),  # noqa E501
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
