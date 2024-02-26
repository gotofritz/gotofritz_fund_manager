from django.urls import path, re_path
from .views import ActiveFundList, SingleFund, home

urlpatterns = [
    path("", home, name="home"),
    re_path(r"^api/funds/?$", ActiveFundList.as_view(), name="active_funds"),
    re_path(r"^api/fund/(?P<pk>\d+)/?$", SingleFund.as_view(), name="single_fund"),
]
