from 臺灣言語工具.系統整合.程式腳本 import 程式腳本
import http
from itertools import zip_longest
import json
from os.path import join
from shutil import copyfile
from tempfile import TemporaryDirectory
from urllib.parse import quote

from siunn1ua2ah4.settings import I7SIAT4_TOO5


from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.解析整理.文章粗胚 import 文章粗胚
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音


class 做影片(程式腳本):

    @classmethod
    def 使用者提供的資料(cls, 圖陣列, 聲陣列, 文字陣列, 存檔所在):
        with TemporaryDirectory() as 目錄:
            字陣列 = cls.轉文本資料(文字陣列, 目錄)
            cls.收著資料(圖陣列, 聲陣列, 字陣列, 存檔所在)

    @classmethod
    def 收著資料(cls, 圖陣列, 聲陣列, 字陣列, 存檔所在):
        with TemporaryDirectory() as 目錄:
            新聲陣列 = []
            for 第幾个, (聲, 字) in enumerate(zip_longest(聲陣列, 字陣列)):
                if 聲 is not None:
                    新聲陣列.append(聲)
                else:
                    新聲陣列.append(cls.揣聲音(字, join(目錄, '{}.wav'.format(第幾个))))
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
            敆做伙結果檔 = join(目錄, 'result.mkv')
            敆做伙指令 = ['mkvmerge']
            敆做伙指令.append('-o')
            敆做伙指令.append(敆做伙結果檔)
            for 結果檔 in 全部結果檔:
                敆做伙指令.append(結果檔)
                敆做伙指令.append('+')
            敆做伙指令.pop()
            cls._走指令(敆做伙指令)

            敆做伙轉換檔 = join(目錄, 'result.mp4')
            上尾轉換指令 = ['avconv']
            上尾轉換指令.append('-i')
            上尾轉換指令.append(敆做伙結果檔)
#             上尾轉換指令.append('-c')
#             上尾轉換指令.append('copy')
            上尾轉換指令.append('-y')
            上尾轉換指令.append(敆做伙轉換檔)
            cls._走指令(上尾轉換指令)

            copyfile(敆做伙轉換檔, 存檔所在)

    @classmethod
    def 轉文本資料(cls, 文字陣列, 目錄):
        漢羅 = '\n'.join(文字陣列)
        conn = http.client.HTTPConnection(
            "xn--lhrz38b.xn--v0qr21b.xn--kpry57d"
        )
        conn.request(
            "GET",
            "/%E6%A8%99%E6%BC%A2%E5%AD%97%E9%9F%B3%E6%A8%99?%E6%9F%A5%E8%A9%A2%E8%85%94%E5%8F%A3=%E9%96%A9%E5%8D%97%E8%AA%9E&%E6%9F%A5%E8%A9%A2%E8%AA%9E%E5%8F%A5=" +
            quote(漢羅)
        )
        r1 = conn.getresponse()
        if r1.status != 200:
            print(r1.status, r1.reason)
            print(漢羅)
            raise RuntimeError()
        字陣列 = []
        for 第幾筆, 資料 in enumerate(json.loads(r1.read().decode('utf-8'))['綜合標音']):
            檔名 = join(目錄, '{}.srt'.format(第幾筆))
            cls._陣列寫入檔案(
                檔名,
                [
                    '1',
                    '00:00:00,000 --> 00:00:00,100',
                    資料['漢字'].strip().replace(' ', ''),
                    資料['臺羅閏號調'].strip()
                ]
            )
            字陣列.append(檔名)
        return 字陣列

    @classmethod
    def 揣聲音(cls, 字, 存檔的所在):
        with open(字) as 檔案:
            *_, 漢字, 臺羅 = 檔案.read().strip().split('\n')
            with open(存檔的所在, 'wb') as 存檔:
                存檔.write(cls.掠聲音(漢字, 臺羅))
            return 存檔的所在

    @classmethod
    def 掠聲音(cls, 漢字, 臺羅):
        句物件 = 拆文分析器.對齊句物件(
            文章粗胚.數字英文中央全加分字符號(漢字), 
            文章粗胚.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 臺羅)
            )
        conn = http.client.HTTPConnection(
            "xn--lhrz38b.xn--v0qr21b.xn--kpry57d"
        )
        conn.request(
            "GET",
            '/%E8%AA%9E%E9%9F%B3%E5%90%88%E6%88%90?' +
            '%E6%9F%A5%E8%A9%A2%E8%85%94%E5%8F%A3=%E9%96%A9%E5%8D%97%E8%AA%9E' +
            '&%E6%9F%A5%E8%A9%A2%E8%AA%9E%E5%8F%A5=' +
            quote(句物件.看分詞())
        )
        r1 = conn.getresponse()
        if r1.status != 200:
            print(r1.status, r1.reason)
            raise RuntimeError()
        return r1.read()
