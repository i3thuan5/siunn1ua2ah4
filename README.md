# 傷倚矣
靈感[來源](https://www.facebook.com/plugins/video.php?href=https%3A%2F%2Fwww.facebook.com%2F100000731913117%2Fvideos%2F1544929298874786%2F&show_text=0&width=560)


### 腳本
```
sudo apt-get install -y language-pack-zh-hant fonts-wqy-microhei
sudo apt-get install -y imagemagick libav-tools libavcodec-extra
sudo apt-get install -y mkvtoolnix 
# 直接做
avconv -i ti1a2.jpg -i huan1ing5.wav -vf subtitles=huan1ing5.srt -s svga -y tmp.avi

avconv -i ti1a2.jpg -i huan1ing5.wav -s svga -y tmp.avi
mkvmerge -o output.avi tmp.avi huan1ing5.srt
```

### 後端程式
```
virtualenv --python=python3 venv; . venv/bin/activate; pip install --upgrade pip # 設置環境檔
pip install line-bot-sdk django tai5-uan5_gian5-gi2_kang1-ku7
```

### Line設定
* [SDK](https://github.com/line/line-bot-sdk-python/tree/6fde69b527229b3d6115fbcd0ef9be499bf54fb5)
* [設定](https://business.line.me/en/)
* [說明](https://devdocs.line.me/en/#send-message-object)
