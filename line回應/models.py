from django.db import models


class 圖片表(models.Model):
    使用者類型 = models.CharField(max_length=200)
    使用者編號 = models.IntegerField()
    檔案 = models.FileField()

    @classmethod
    def 加一張圖(cls, source, content):
        圖 = cls.objects.create(使用者類型=source.type, 使用者編號=source.id)
        圖.檔案.save('圖', b''.join(content))

    @classmethod
    def 全部圖(cls, source, message):
        return cls.objects.filter(使用者類型=source.type, 使用者編號=source.id)
