
from django.conf.urls import url
from line回應.介面 import line介面
from line回應.看影片 import 影片連結

urlpatterns = [
    url(r'^callback/', line介面),
    url(r'^khuann3/(?P<path>.*)$', 影片連結),
]
