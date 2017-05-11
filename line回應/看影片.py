
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
    <a href='/upload/{}' download='siunn7ua2ah4.mp4'>下載影片</a>
</p>
<p>
若出現「不支援檔案下載功能，請透過其他瀏覽器再試一次」，請試「以其他應用程式開啟」的chrome開。<br/>
</p>
<p>
掠落來就會當分享到fb佮line矣
</p>
</body>
"""
        .format(path)
    )
