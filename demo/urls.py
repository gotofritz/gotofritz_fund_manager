from django.urls import path
from .views import ActiveFundList, upload_file, home

urlpatterns = [
    path("", home, name="home"),
    path("upload/", upload_file, name="upload_file"),
    path("api/funds/", ActiveFundList.as_view(), name="active_funds"),
]
