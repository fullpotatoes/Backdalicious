from django.urls import path
from . import views

urlpatterns = [
    path("Plats/", views.PlatListCreate.as_view(), name="Plat-view-create"),
    path('api/test/', views.test_api, name='test'),
]
