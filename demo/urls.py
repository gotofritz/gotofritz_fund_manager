from django.urls import path
from .views import upload_file, home

urlpatterns = [
    path("", home, name="home"),
    path("upload/", upload_file, name="upload_file"),
]
