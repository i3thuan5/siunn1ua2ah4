from 臺灣言語工具.系統整合.程式腳本 import 程式腳本
import http
from itertools import zip_longest
import json
from os.path import join
from tempfile import TemporaryDirectory
from urllib.parse import quote
import ssl
from siunn1ua2ah4.settings import I7SIAT4_TOO5


from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.解析整理.文章粗胚 import 文章粗胚

ssl.match_hostname = lambda cert, hostname: True


class 做影片(程式腳本):

    @classmethod
    def 使用者提供的資料(cls, 腔口參數, 圖陣列, 聲陣列, 文字陣列, 影片存檔所在, 縮圖存檔所在):
        with TemporaryDirectory() as 目錄:
            字幕檔陣列,分詞陣列 = cls.轉文本資料(腔口參數, 文字陣列, 目錄)
            cls.收著資料(腔口參數, 圖陣列, 聲陣列, 字幕檔陣列,分詞陣列, 影片存檔所在)
            cls._走指令([
                'avconv',
                '-i', 影片存檔所在,
                '-r', '10',
                '-t', '0.1',
                '-s', 'qqvga',
                '-y',
                縮圖存檔所在
            ])

    @classmethod
    def 收著資料(cls, 腔口參數, 圖陣列, 聲陣列, 字幕檔陣列,分詞陣列, 存檔所在):
        with TemporaryDirectory() as 目錄:
            新聲陣列 = []
            for 第幾个, (聲, 分詞) in enumerate(zip_longest(聲陣列, 分詞陣列)):
                if 聲 is not None:
                    新聲陣列.append(聲)
                else:
                    新聲陣列.append(
                        cls.揣聲音(腔口參數, 分詞, join(目錄, '{}.wav'.format(第幾个)))
                        )
            if len(圖陣列) == 0:
                新圖陣列 = [I7SIAT4_TOO5] * len(字幕檔陣列)
            else:
                新圖陣列 = []
                while len(新圖陣列) < len(字幕檔陣列):
                    新圖陣列.append(圖陣列[len(新圖陣列) % len(圖陣列)])
            cls.敆做伙(新圖陣列, 新聲陣列, 字幕檔陣列, 存檔所在)

    @classmethod
    def 敆做伙(cls, 圖陣列, 聲陣列, 字幕檔陣列, 存檔所在):
        with TemporaryDirectory() as 目錄:
            全部結果表 = join(目錄, 'tuan.pio')
            with open(全部結果表, 'w') as 表:
                for 第幾个, (圖, 聲, 字幕檔) in enumerate(zip(圖陣列, 聲陣列, 字幕檔陣列)):
                    結果檔 = join(目錄, 'output{}.mp4'.format(第幾个))
                    暫時圖 = join(目錄, 'jpg{}.jpg'.format(第幾个))
                    cls._走指令([
                        'convert',
                        圖,
                        暫時圖,
                    ])
                    cls._走指令([
                        'avconv',
                        '-i', 暫時圖, '-i', 聲, '-vf', 'subtitles={}'.format(字幕檔),
                        '-s', 'svga', '-y', 結果檔,
                    ])
                    print("file '{}'".format(結果檔), file=表)

            敆做伙指令 = [
                'ffmpeg',
                '-f', 'concat',
                '-safe', '0',
                '-i', 全部結果表,
                '-c', 'copy',
                '-y',
                存檔所在
            ]
            cls._走指令(敆做伙指令)

    @classmethod
    def 轉文本資料(cls, 腔口參數, 文字陣列, 目錄):
        漢羅陣列 = []
        for 文字 in 文字陣列:
            for 一逝 in 文字.split('\n'):
                if len(一逝.strip()) != 0:
                    漢羅陣列.append(一逝.strip())
        漢羅 = '\n'.join(漢羅陣列)
        conn = http.client.HTTPSConnection(
            "xn--lhrz38b.xn--v0qr21b.xn--kpry57d"
        )
        conn.request(
            "GET",
            "/{}?{}={}&{}={}".format(
                quote('標漢字音標'),
                quote('查詢腔口'),
                quote(腔口參數['服務腔口']),
                quote('查詢語句'),
                quote(漢羅),
            )
        )
        r1 = conn.getresponse()
        if r1.status != 200:
            print(r1.status, r1.reason)
            print(漢羅)
            raise RuntimeError()
        字幕檔陣列 = []
        分詞陣列 = []
        for 第幾筆, 資料 in enumerate(
            json.loads(r1.read().decode('utf-8'))[腔口參數['資料來源']]
        ):
            檔名 = join(目錄, '{}.srt'.format(第幾筆))
            cls._陣列寫入檔案(
                檔名,
                [
                    '1',
                    '00:00:00,000 --> 00:00:00,100',
                    資料['漢字'].strip(),
                    資料[腔口參數['標音欄位']].strip()
                ]
            )
            字幕檔陣列.append(檔名)
            分詞陣列.append(資料['分詞'])
        return 字幕檔陣列,分詞陣列

    @classmethod
    def 揣聲音(cls, 腔口參數, 分詞, 存檔的所在):
            with open(存檔的所在, 'wb') as 存檔:
                存檔.write(cls.掠聲音(腔口參數, 分詞))
            return 存檔的所在

    @classmethod
    def 掠聲音(cls, 腔口參數, 分詞):
        domain = "xn--lhrz38b.xn--v0qr21b.xn--kpry57d"
        網址 = "/{}?{}={}&{}={}".format(
            quote('語音合成'),
            quote('查詢腔口'),
            quote(腔口參數['服務腔口']),
            quote('查詢語句'),
            quote(分詞),
        )

        conn = http.client.HTTPSConnection(domain)
        conn.request("GET", 網址)
        r1 = conn.getresponse()
        if r1.status != 200:
            raise RuntimeError('連線錯誤：{}{}\n{} {}'.format(
                domain, 網址, r1.status, r1.reason
            ))
        return r1.read()
