from os.path import abspath, dirname, join, isfile

from django.test.testcases import TestCase
from 鬥做伙.做影片 import 做影片


class 敆檔案試驗(TestCase):
    def setUp(self):
        self.目錄 = join(dirname(abspath(__file__)), '..', '圖')
        self.圖 = join(self.目錄, 'ti1a2.jpg')
        self.音 = join(self.目錄, 'huan1ing5.wav')
        self.字 = join(self.目錄, 'huan1ing5.srt')

    def test_一組(self):
        檔案的所在 = 做影片.敆做伙([self.圖], [self.音], [self.字])
        self.assertTrue(isfile(檔案的所在))
