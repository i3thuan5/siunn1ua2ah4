import re


class 指令:
    腔口比對 = {
        '臺語': re.compile('(([台臺]語)|(([台臺]灣)?閩南語))[：:]'),
    }

    @classmethod
    def 判斷腔口(cls, 語句):
        for 腔口, 比對 in cls.腔口比對.items():
            結果 = 比對.match(語句)
            if 結果:
                return (腔口, 語句[結果.end():])
        return (None, 語句)
