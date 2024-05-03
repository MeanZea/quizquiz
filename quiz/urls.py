from django.urls import include, path

from .views import helloAPI

urlpatterns = [
    path("hello/", helloAPI),
]