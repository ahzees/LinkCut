from django.urls import path

from .views import if_exist, redirect_to

urlpatterns = [path("", if_exist), path("<str:pk>/", redirect_to)]
