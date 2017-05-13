from os.path import join

from django.conf import settings
from django.core.files.base import ContentFile
from django.db import models

from siunn1ua2ah4.settings import DOMAIN


from 鬥做伙.做影片 import 做影片


class 圖片表(models.Model):
    使用者類型 = models.CharField(max_length=200)
    使用者編號 = models.CharField(max_length=200)
    檔案 = models.FileField()

    @classmethod
    def _提著編號(cls, source):
        if source.type == 'user':
            return source.user_id
        if source.type == 'group':
            return source.group_id
#         if source.type=='room'
        return source.room_id

    @classmethod
    def 加一張圖(cls, source, content):
        圖 = cls.objects.create(使用者類型=source.type, 使用者編號=cls._提著編號(source))
        圖.檔案.save('image', ContentFile(b''.join(content)))

    @classmethod
    def 全部圖(cls, source):
        return cls.objects.filter(使用者類型=source.type, 使用者編號=cls._提著編號(source))

    def 檔案路徑(self):
        return join(settings.MEDIA_ROOT, self.檔案.name)

    def delete(self):
        self.檔案.delete()
        super(圖片表, self).delete()


class 結果影片表(models.Model):
    檔案 = models.FileField()
    縮圖 = models.FileField()

    @classmethod
    def 加影片(cls, 全部圖, 聲陣列, 文字陣列):
        圖陣列 = []
        for 圖 in 全部圖:
            圖陣列.append(圖.檔案路徑())
        結果影片 = cls.objects.create()
        結果影片.檔案.save('result', ContentFile(b''))
        結果影片.縮圖.save('result', ContentFile(b''))
        做影片.使用者提供的資料(
            圖陣列, 聲陣列, 文字陣列,
            結果影片.影片檔案路徑(), 結果影片.影片縮圖路徑()
        )
        return 結果影片

    def 影片檔案路徑(self):
        return join(settings.MEDIA_ROOT, self.檔案.name)

    def 影片網址(self):
        return DOMAIN + self.檔案.url

    def 影片縮圖路徑(self):
        return join(settings.MEDIA_ROOT, self.縮圖.name)

    def 縮圖網址(self):
        return DOMAIN + self.縮圖.url

    def 網頁下載網址(self):
        return DOMAIN + self.檔案.url.replace('/upload/', '/khuann3/')
