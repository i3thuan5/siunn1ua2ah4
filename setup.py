from distutils.core import setup
from os import walk


def 揣工具包(頭):
    'setup的find_packages無支援windows中文檔案'
    工具包 = []
    for 目錄, _, 檔案 in walk(頭):
        if '__init__.py' in 檔案:
            工具包.append(目錄.replace('/', '.'))
    return 工具包


github網址 = 'https://github.com/i3thuan5/siunn1ua2ah4'


setup(
    name='siunn1-ua2--ah4',
    packages=揣工具包('line回應') + 揣工具包('鬥做伙'),
    version='0.0.2',
    description='母語影片製作',
    long_description='母語影片製作，傳圖佮字幕，幫你做影片～～',
    author='薛丞宏',
    author_email='ihcaoe@gmail.com',
    url='https://xn--v0qr21b.xn--kpry57d/',
    download_url=github網址,
    keywords=[
         '語言合成',
        'Text to Speech',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Operating System :: Unix',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    install_requires=[
        'tai5-uan5_gian5-gi2_kang1-ku7',
        'django',
        'line-bot-sdk',
    ],
)
