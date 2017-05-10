
from django.conf.urls import url
from line回應.介面 import line介面

urlpatterns = [
    url(r'^callback/', line介面),
]
