from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ArchiveViewSet

router = DefaultRouter()
router.register(r'archives', ArchiveViewSet)

urlpatterns = [
    path('', include(router.urls)),
]