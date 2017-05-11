
from django.http.response import HttpResponse


def 影片連結(request, path):
    return HttpResponse(
        """
<doctype html>
<head>
  <style type='text/css'>
  html {{
    font-size: 300%;
  }}
  </style>
</head>
<body>
<h1>傷倚矣 - 生影片</h1>
<p>
    <a href='/upload/{}' download>下載影片</a>
</p>
<p>
若出現「不支援檔案下載功能」，無法度掠影片，請試正爿面頂目錄「以其他應用程式開啟」的chrome開。<br/>
</p>
<p>
掠落來就會當分享到fb佮line矣
</p>
</body>
"""
        .format(path)
    )
