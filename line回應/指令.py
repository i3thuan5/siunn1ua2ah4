import re


class 指令:
    符號 = '[：:]'
    腔口比對 = {
        '臺語': re.compile('(([台臺]語)|(([台臺]灣)?閩南語))' + 符號),
        '四縣': re.compile('((客語)|(客家話))?四縣[腔話]?' + 符號),
        '海陸': re.compile('((客語)|(客家話))?海陸[腔話]?' + 符號),
        '大埔': re.compile('((客語)|(客家話))?大埔[腔話]?' + 符號),
        '饒平': re.compile('((客語)|(客家話))?饒平[腔話]?' + 符號),
        '詔安': re.compile('((客語)|(客家話))?詔安[腔話]?' + 符號),
        'Pangcah': re.compile(
            '((Pangcah)|(Amis)|(阿美語?))' + 符號, flags=re.IGNORECASE
        ),
    }

    @classmethod
    def 判斷腔口(cls, 語句):
        for 腔口, 比對 in cls.腔口比對.items():
            結果 = 比對.match(語句)
            if 結果:
                return (腔口, 語句[結果.end():])
        return (None, 語句)
