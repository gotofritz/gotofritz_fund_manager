from django.shortcuts import render
from demo.models import STRATEGY_CHOICES, Fund
from demo.services import process_uploaded_file
from .forms import UploadFileForm
from django.http import HttpRequest
from django.http.response import HttpResponse
from .tables import FundsTable
from django_tables2 import RequestConfig


def home(request: HttpRequest) -> HttpResponse:
    return render(request, "demo/upload.html")


def upload_file(request: HttpRequest) -> HttpResponse:
    context = {
        "form": UploadFileForm(),
        "error": None,
        "success": False,
        "funds": [],
        "strategies": STRATEGY_CHOICES,
        "funds_count": 0,
    }

    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            error = process_uploaded_file(request.FILES["file"])
            if error:
                context["error"] = error
                context["form"] = form
            else:
                context["success"] = True
        else:
            context["form"] = form

    strategy_filter = request.GET.get("strategy_filter", None)
    if strategy_filter:
        queryset = Fund.objects.filter(active=True, strategy=strategy_filter)
    else:
        queryset = Fund.objects.filter(active=True)
    context["funds_count"] = queryset.count()

    table = FundsTable(queryset)
    RequestConfig(request).configure(table)

    context["table"] = table
    return render(request, "demo/upload.html", context)
