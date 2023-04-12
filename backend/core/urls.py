from django.urls import include, path
from rest_framework import routers

from backend.core.views import DocumentViewSet

app_name = 'core'

router = routers.DefaultRouter()

router.register(r'documentos', DocumentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
