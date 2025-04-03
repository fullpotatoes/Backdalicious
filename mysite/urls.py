# projet/urls.py
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import PlatViewSet  # Remplacez app_name par le nom de votre application

router = DefaultRouter()
router.register(r'plats', PlatViewSet, basename='plat')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]