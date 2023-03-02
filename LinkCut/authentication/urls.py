from django.urls import include, path
from rest_framework.routers import SimpleRouter

from .views import DetailCustomUserApiView, ListCustomUserApiView

router = SimpleRouter()
router.register("users", ListCustomUserApiView)
router.register("user", DetailCustomUserApiView)
urlpatterns = [
    path("api/v1/", include(router.urls)),
    path("api/v1/drf-auth/", include("rest_framework.urls")),
]
