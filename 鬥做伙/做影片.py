from 臺灣言語工具.系統整合.程式腳本 import 程式腳本
from os.path import join
from tempfile import TemporaryDirectory


class 做影片(程式腳本):
    @classmethod
    def 敆做伙(cls, 圖陣列, 音檔陣列, 字幕陣列, 存檔所在):
        with TemporaryDirectory() as 目錄:
            全部結果檔=[]
            for 第幾个, (圖, 音檔, 字幕) in enumerate(zip(圖陣列, 音檔陣列, 字幕陣列)):
                暫時檔 = join(目錄, 'tmp{}.avi'.format(第幾个))
                結果檔 = join(目錄, 'output{}.mkv'.format(第幾个))
                cls._走指令([
                    'avconv',
                    '-i', 圖, '-i', 音檔,
                    '-s', 'svga', '-y', 暫時檔,
                ])
                cls._走指令([
                    'mkvmerge',
                    '-o', 結果檔,
                    暫時檔, 字幕,
                ])
                全部結果檔.append(結果檔)
#                 mkvmerge -o 1.mkv 1-1.mkv + 1-2.mkv + 1-3.mkv
            敆做伙結果檔 = join(目錄, 'result{}.mkv'.format(第幾个))
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
            上尾轉換指令.append('-c')
            上尾轉換指令.append('copy')
            上尾轉換指令.append('-y')
            上尾轉換指令.append(存檔所在)
            cls._走指令(上尾轉換指令)
