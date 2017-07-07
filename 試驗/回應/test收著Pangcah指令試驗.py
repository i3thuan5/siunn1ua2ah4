from django.test.testcases import TestCase


from line回應.指令 import 指令


class 收著Pangcah指令試驗(TestCase):
    def tearDown(self):
        self.assertEqual(指令.判斷腔口(self.指令), self.判斷)

    def test_Pangcah(self):
        self.指令 = "Pangcah：nga'ay ho?"
        self.判斷 = ('Pangcah',  "nga'ay ho?")

    def test_AMIS(self):
        self.指令 = "AMIS：nga'ay ho?"
        self.判斷 = ('Pangcah',  "nga'ay ho?")

    def test_阿美語(self):
        self.指令 = "阿美語:nga'ay ho?"
        self.判斷 = ('Pangcah',  "nga'ay ho?")

    def test_阿美(self):
        self.指令 = "阿美:nga'ay ho?"
        self.判斷 = ('Pangcah',  "nga'ay ho?")
