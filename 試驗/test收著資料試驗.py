from os.path import abspath, dirname, join
from tempfile import TemporaryDirectory
from unittest.mock import patch

from django.test.testcases import TestCase

from siunn1ua2ah4.settings import I7SIAT4_TOO5


from 鬥做伙.做影片 import 做影片


@patch('鬥做伙.做影片.做影片.敆做伙')
class 收著資料試驗(TestCase):
    def setUp(self):
        self.目錄 = join(dirname(abspath(__file__)), '..', '圖')
        self.圖 = join(self.目錄, 'ti1a2.jpg')
        self.音 = join(self.目錄, 'huan1ing5.wav')
        self.字幕 = join(self.目錄, 'huan1ing5.srt')
        self.分詞 = '逐-家｜tak8-ke1 做-伙｜tso3-hue2 來｜lai5- 𨑨-迌｜tshit4-tho5 ！'

    def test_無圖用預設圖(self, 敆做伙mock):
        with TemporaryDirectory() as 目錄:
            檔案的所在 = join(目錄, 'a.mp4')
            做影片.收著資料('閩南語', [], [self.音], [self.字幕],  [self.分詞], 檔案的所在)
            敆做伙mock.assert_called_once_with(
                [I7SIAT4_TOO5], [self.音], [self.字幕], 檔案的所在
            )

    def test_圖無夠愛循環用(self, 敆做伙mock):
        with TemporaryDirectory() as 目錄:
            檔案的所在 = join(目錄, 'a.mp4')
            做影片.收著資料(
                '閩南語',
                ['a.jpg', 'b.jpg'],
                [self.音, self.音, self.音],
                [self.字幕, self.字幕, self.字幕],
                [self.分詞, self.分詞, self.分詞],
                檔案的所在
            )
            敆做伙mock.assert_called_once_with(
                ['a.jpg', 'b.jpg', 'a.jpg'],
                [self.音, self.音, self.音],
                [self.字幕, self.字幕, self.字幕],
                檔案的所在
            )

    @patch('鬥做伙.做影片.做影片.揣聲音')
    def test_無音用合成音(self, 揣聲音mock, 敆做伙mock):
        揣聲音mock.return_value = self.音
        with TemporaryDirectory() as 目錄:
            檔案的所在 = join(目錄, 'a.mp4')
            做影片.收著資料('閩南語', [self.圖], [], [self.字幕], [self.分詞], 檔案的所在)
            敆做伙mock.assert_called_once_with(
                [self.圖], [self.音], [self.字幕], 檔案的所在
            )
