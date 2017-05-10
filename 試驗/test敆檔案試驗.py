from os.path import abspath, dirname, join, isfile
from tempfile import TemporaryDirectory

from django.test.testcases import TestCase


from 鬥做伙.做影片 import 做影片


class 敆檔案試驗(TestCase):
    def setUp(self):
        self.目錄 = join(dirname(abspath(__file__)), '..', '圖')
        self.圖 = join(self.目錄, 'ti1a2.jpg')
        self.音 = join(self.目錄, 'huan1ing5.wav')
        self.字 = join(self.目錄, 'huan1ing5.srt')

    def test_一組(self):
        with TemporaryDirectory() as 目錄:
            檔案的所在 = join(目錄, 'a.mp4')
            做影片.敆做伙([self.圖], [self.音], [self.字], 檔案的所在)
            self.assertTrue(isfile(檔案的所在))

    def test_兩組(self):
        with TemporaryDirectory() as 目錄:
            檔案的所在 = join(目錄, 'b.avi')
            做影片.敆做伙([self.圖, self.圖], [self.音, self.音],
                    [self.字, self.字], 檔案的所在)
            self.assertTrue(isfile(檔案的所在))

    def test_兩組的檔案佮一組無仝(self):
        with TemporaryDirectory() as 目錄:
            一組檔案的所在 = join(目錄, 'c.avi')
            做影片.敆做伙([self.圖], [self.音], [self.字], 一組檔案的所在)
            兩組檔案的所在 = join(目錄, 'd.avi')
            做影片.敆做伙(
                [self.圖, self.圖],
                [self.音, self.音],
                [self.字, self.字],
                兩組檔案的所在
            )
            with open(一組檔案的所在, 'rb') as 一組檔案:
                with open(兩組檔案的所在, 'rb') as 兩組檔案:
                    self.assertNotEqual(一組檔案.read(), 兩組檔案.read())
