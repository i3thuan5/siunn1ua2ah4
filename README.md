# 傷倚矣
靈感[來源](https://www.facebook.com/plugins/video.php?href=https%3A%2F%2Fwww.facebook.com%2F100000731913117%2Fvideos%2F1544929298874786%2F&show_text=0&width=560)


### 腳本
```
sudo apt-get install mkvtoolnix
avconv -i ti1a2.jpg -i huan1ing5.wav -s svga -y tmp.avi
mkvmerge -o output.avi tmp.avi huan1ing5.srt
```

### 後端程式
```
virtualenv --python=python3 venv; . venv/bin/activate; pip install --upgrade pip # 設置環境檔
pip install line-bot-sdk flask django
```
