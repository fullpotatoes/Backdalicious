from django.urls import path
from api import views

urlpatterns = [
    path("Plat/", views.PlatListCreate.as_view(), name="Plat-view-create"),
]
