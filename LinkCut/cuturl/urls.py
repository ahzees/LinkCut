from django.urls import include, path
from rest_framework.routers import DefaultRouter, SimpleRouter

from . import views

router = DefaultRouter()
router.register(r"url", views.UrlApiView, basename="url")

urlpatterns = [
    path("", views.if_exist),
    path("<str:pk>/", views.redirect_to),
    path("api/v1/", include(router.urls)),
]
