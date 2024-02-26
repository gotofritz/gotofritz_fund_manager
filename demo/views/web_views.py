import logging
from django.shortcuts import render
from demo.models import STRATEGY_CHOICES, Fund
from demo.services import process_uploaded_file
from ..forms import UploadFileForm
from django.http import HttpRequest
from django.http.response import HttpResponse
from ..tables import FundsTable
from django_tables2 import RequestConfig
from django.views.generic import View
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django_tables2 import RequestConfig
from ..forms import UploadFileForm
from ..models import Fund, STRATEGY_CHOICES
from ..tables import FundsTable
from ..services import process_uploaded_file

logger = logging.getLogger(__name__)


def get_form_errors(form):
    error_messages = []
    for _, errors in form.errors.items():
        for error in errors:
            error_messages.append(str(error))

    return (
        f"<ul><li>{ '</li><li>'.join(error_messages) }</li></ul>"
        if error_messages
        else ""
    )


class HomeView(View):
    template_name = "demo/home.html"
    form_class = UploadFileForm

    def get_context(self, request: HttpRequest, form=None):
        strategy_filter = request.GET.get("strategy_filter", None)
        if strategy_filter:
            queryset = Fund.objects.filter(active=True, strategy=strategy_filter)
        else:
            queryset = Fund.objects.filter(active=True)

        funds_count = queryset.count()
        table = FundsTable(queryset)
        RequestConfig(request).configure(table)

        return {
            "form": form if form is not None else self.form_class(),
            "error": None,
            "success": False,
            "funds": [],
            "strategies": STRATEGY_CHOICES,
            "funds_count": funds_count,
            "table": table,
        }

    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        context = self.get_context(request)
        return render(request, self.template_name, context)

    def post(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        form = self.form_class(request.POST, request.FILES)
        context = self.get_context(request, form)
        if form.is_valid():
            error = process_uploaded_file(request.FILES["file"])
        else:
            error = get_form_errors(form)

        context = self.get_context(request, form)
        if error:
            context["error"] = error
            logger.error(f"Errors uploading list of funds: {error}")
        else:
            context["success"] = True
        return render(request, self.template_name, context)
