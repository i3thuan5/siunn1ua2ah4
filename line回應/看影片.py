
from django.http.response import HttpResponse


def 影片連結(request, path):
    return HttpResponse(
        """
<doctype html>
<body>
<a href='/upload/{}' download>下載影片</a><br/>
若無法度掠影片，請試正爿面頂目錄「以其他應用程式開啟」的chrome開。<br/>
掠落來就會當分享矣
</body>
"""
        .format(path)
    )
