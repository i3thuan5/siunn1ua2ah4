from django.db import models
from django.core.files.base import ContentFile


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
        圖.檔案.save('圖', ContentFile(b''.join(content)))

    @classmethod
    def 全部圖(cls, source, message):
        return cls.objects.filter(使用者類型=source.type, 使用者編號=cls._提著編號(source))
