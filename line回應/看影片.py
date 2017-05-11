
from django.http.response import HttpResponse


def 影片連結(request, path):
    return HttpResponse(
        "<a href='/upload/{}' download>ss</a>".format(path)
    )
