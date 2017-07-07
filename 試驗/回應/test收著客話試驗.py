from django.test.testcases import TestCase


from line回應.指令 import 指令


class 收著客話指令試驗(TestCase):
    def tearDown(self):
        self.assertEqual(指令.判斷腔口(self.指令), self.判斷)

    def test_四縣(self):
        self.指令 = '四縣：食飽吂？'
        self.判斷 = ('四縣', '食飽吂？')

    def test_海陸腔(self):
        self.指令 = '海陸腔:食飽吂？'
        self.判斷 = ('海陸', '食飽吂？')

    def test_客家話大埔腔(self):
        self.指令 = '客家話大埔腔:食飽吂？'
        self.判斷 = ('大埔', '食飽吂？')

    def test_客語饒平(self):
        self.指令 = '客語饒平:食飽吂？'
        self.判斷 = ('饒平', '食飽吂？')

    def test_詔安話(self):
        self.指令 = '詔安話:食飽吂？'
        self.判斷 = ('詔安', '食飽吂？')
