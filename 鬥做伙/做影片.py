from 臺灣言語工具.系統整合.程式腳本 import 程式腳本
from os.path import join
from tempfile import TemporaryDirectory
from itertools import zip_longest
from siunn1ua2ah4.settings import I7SIAT4_TOO5


class 做影片(程式腳本):
    @classmethod
    def 收著資料(cls, 圖陣列, 聲陣列, 字陣列, 存檔所在):
        新聲陣列 = []
        for 聲, 文本 in zip_longest(聲陣列, 字陣列):
            if 聲 is not None:
                新聲陣列.append(聲)
            else:
                新聲陣列.append(cls.揣聲音(文本))
        if len(圖陣列) == 0:
            新圖陣列 = [I7SIAT4_TOO5] * len(字陣列)
        else:
            新圖陣列 = []
            while len(新圖陣列) < len(字陣列):
                新圖陣列.append(圖陣列[len(新圖陣列) % len(圖陣列)])
        cls.敆做伙(新圖陣列, 新聲陣列, 字陣列, 存檔所在)

    @classmethod
    def 敆做伙(cls, 圖陣列, 聲陣列, 字陣列, 存檔所在):
        with TemporaryDirectory() as 目錄:
            全部結果檔 = []
            for 第幾个, (圖, 聲, 字) in enumerate(zip(圖陣列, 聲陣列, 字陣列)):
                結果檔 = join(目錄, 'output{}.mkv'.format(第幾个))
                cls._走指令([
                    'avconv',
                    '-i', 圖, '-i', 聲, '-vf', 'subtitles={}'.format(字),
                    '-s', 'svga', '-y', 結果檔,
                ])
                全部結果檔.append(結果檔)
            敆做伙結果檔 = join('result.mkv')
            敆做伙指令 = ['mkvmerge']
            敆做伙指令.append('-o')
            敆做伙指令.append(敆做伙結果檔)
            for 結果檔 in 全部結果檔:
                敆做伙指令.append(結果檔)
                敆做伙指令.append('+')
            敆做伙指令.pop()
            cls._走指令(敆做伙指令)

            上尾轉換指令 = ['avconv']
            上尾轉換指令.append('-i')
            上尾轉換指令.append(敆做伙結果檔)
#             上尾轉換指令.append('-c')
#             上尾轉換指令.append('copy')
            上尾轉換指令.append('-y')
            上尾轉換指令.append(存檔所在)
            cls._走指令(上尾轉換指令)

    @classmethod
    def 揣聲音(cls, 字):
        pass
