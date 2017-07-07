from django.test.testcases import TestCase


from line回應.指令 import 指令


class 收著臺語指令試驗(TestCase):
    def tearDown(self):
        self.assertEqual(指令.判斷腔口(self.指令), self.判斷)

    def test_台語全形(self):
        self.指令 = '台語：食飽未？'
        self.判斷 = ('臺語', '食飽未？')

    def test_臺語半形(self):
        self.指令 = '臺語:食飽未？'
        self.判斷 = ('臺語', '食飽未？')

    def test_閩南語(self):
        self.指令 = '閩南語:食飽未？'
        self.判斷 = ('臺語', '食飽未？')

    def test_台灣閩南語(self):
        self.指令 = '台灣閩南語:食飽未？'
        self.判斷 = ('臺語', '食飽未？')

    def test_臺灣閩南語(self):
        self.指令 = '臺灣閩南語:食飽未？'
        self.判斷 = ('臺語', '食飽未？')
