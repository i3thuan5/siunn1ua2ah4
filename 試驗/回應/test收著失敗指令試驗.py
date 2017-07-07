from django.test.testcases import TestCase


from line回應.指令 import 指令


class 收著失敗指令試驗(TestCase):
    def tearDown(self):
        self.assertEqual(指令.判斷腔口(self.指令), (None, self.指令))

    def test_無腔口(self):
        self.指令 = '食飽未？'

    def test_半形(self):
        self.指令 = ':食飽未？'
