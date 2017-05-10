import http
from urllib.parse import quote

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, AudioSendMessage, AudioMessage,
    VideoSendMessage
)
import json
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt


line_bot_api = LineBotApi(settings.YOUR_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(settings.YOUR_CHANNEL_SECRET)


@csrf_exempt
def line介面(request):
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent)
#@handler.add(MessageEvent, message=AudioMessage)
#@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    資料 = event.message.text
    original_content_url = (
        'https://xn--lhrz38b.xn--v0qr21b.xn--kpry57d' +
        '/%E8%AA%9E%E9%9F%B3%E5%90%88%E6%88%90' +
        '?%E6%9F%A5%E8%A9%A2%E8%85%94%E5%8F%A3=%E9%96%A9%E5%8D%97%E8%AA%9E&' +
        '%E6%9F%A5%E8%A9%A2%E8%AA%9E%E5%8F%A5=' +
        quote(揣分詞(資料))
    )
    line_bot_api.reply_message(
        event.reply_token,
        [
            TextSendMessage(text=資料, ),
            TextSendMessage(text=original_content_url, ),
            VideoSendMessage(original_content_url='https://www.dropbox.com/s/j69523t6bm9xz3g/Special_Course.mp4?dl=0',
                             preview_image_url='https://itaigi.tw/121c4ed080e9127a72d31ae85d1458fc.svg',
                             ),
            #       AudioSendMessage(original_content_url=original_content_url,
            #    duration=500
            # ),
        ]
    )


def 揣分詞(音標):
    conn = http.client.HTTPConnection("xn--lhrz38b.xn--v0qr21b.xn--kpry57d")
    conn.request(
        "GET",
        "/%E6%A8%99%E6%BC%A2%E5%AD%97%E9%9F%B3%E6%A8%99?%E6%9F%A5%E8%A9%A2%E8%85%94%E5%8F%A3=%E9%96%A9%E5%8D%97%E8%AA%9E&%E6%9F%A5%E8%A9%A2%E8%AA%9E%E5%8F%A5=" +
        quote(音標)
    )
    r1 = conn.getresponse()
    if r1.status != 200:
        print(r1.status, r1.reason)
        print(音標)
        return '服務錯誤'
    data1 = r1.read()  # This will return entire content.
    return json.loads(data1.decode('utf-8'))['分詞']
