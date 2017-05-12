from os.path import abspath, dirname, join
from tempfile import TemporaryDirectory

from django.test.testcases import TestCase


from 鬥做伙.做影片 import 做影片


class 使用者提供的資料試驗(TestCase):
    def setUp(self):
        self.目錄 = join(dirname(abspath(__file__)), '..')
        self.音 = join(self.目錄, '圖', 'huan1ing5.wav')
        self.字 = join(self.目錄, '圖', 'huan1ing5.srt')

    def test_產生檔案看覓(self):
        做影片.使用者提供的資料([], [], ['逐家好', '我是媠豬'], join(self.目錄, 'sui.mp4'))

    def test_有空逝(self):
        with TemporaryDirectory() as 目錄:
            做影片.使用者提供的資料([], [], ['逐家好','', '我是媠豬'], join(目錄, 'sui.mp4'))

    def test_組合圖的檔頭(self):
        with TemporaryDirectory() as 目錄:
            self.組合圖 = join(self.目錄, '圖', 'image_oyuxYDl')
            做影片.使用者提供的資料(
                [self.組合圖], [], ['逐家好', '我是媠豬'],
                join(目錄, 'sui.mp4')
            )
