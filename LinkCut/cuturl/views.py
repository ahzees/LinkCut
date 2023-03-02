# from django.http.respo
# Create your views here
import json
import random

from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect, render
from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from .models import Url
from .serializers import UrlSerializer


class UrlApiView(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet,
):

    serializer_class = UrlSerializer

    def get_queryset(self):
        pk = self.kwargs.get("pk")
        if pk:
            return Url.objects.filter(pk=pk)
        return Url.objects.all()


def encrypt(full_url):
    x = ""
    for i in range(9):
        x += str(random.randint(1, 9))
    if not x in Url.objects.values_list("cut_url"):
        return x


def if_exist(request, x=None):
    if request.method == "POST":
        try:
            x = Url.objects.get(full_url=request.POST.get("long_url"))
        except ObjectDoesNotExist:
            x = Url.objects.create(
                full_url=request.POST.get("long_url"),
                cut_url=encrypt(request.POST.get("long_url")),
            )
        finally:
            x.user.add(request.user)
            return render(
                request,
                "base.html",
                context={
                    "short_url": "http://127.0.0.1:8000/" + x.cut_url,
                },
            )
    return render(request, "base.html")


def redirect_to(request, pk):
    try:
        x = Url.objects.get(cut_url=str(pk)).full_url
    except ObjectDoesNotExist:
        x = "/"
    return redirect(x)
