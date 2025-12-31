from django.urls import path
from .views import log_ip

urlpatterns=[
    path("log_ip/",log_ip),
]