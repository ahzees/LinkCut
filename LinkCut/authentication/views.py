from cuturl.models import Url
from cuturl.serializers import UrlSerializer
from django.shortcuts import render
from rest_framework import mixins
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.decorators import action, permission_classes
from rest_framework.permissions import (
    IsAdminUser,
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
)
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from . import serializers as sr
from .models import CustomUser
from .permissions import IsAuthor


class ListCustomUserApiView(
    mixins.ListModelMixin, mixins.CreateModelMixin, GenericViewSet
):

    serializer_class = sr.CustomUserSerializer
    queryset = CustomUser.objects.all()
    permission_classes = (IsAdminUser,)


class DetailCustomUserApiView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet,
):
    serializer_class = sr.CustomUserSerializer
    queryset = CustomUser.objects.all()
    permission_classes = (IsAuthor,)

    @action(detail=True, methods=["get"], permission_classes=(IsAuthor,))
    def url(self, request, pk):
        if request.user.pk == int(pk):
            return Response(
                {
                    "urls": Url.objects.filter(user__pk=pk).values_list(
                        "pk", "full_url", "cut_url"
                    )
                }
            )
        return Response(
            {"detail": "You do not have permission to perform this action."}
        )
