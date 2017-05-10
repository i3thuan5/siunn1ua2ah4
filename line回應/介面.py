import http
import json
from urllib.parse import quote

from django.conf import settings
from django.http.response import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, AudioMessage,
    TextSendMessage, VideoSendMessage
)
from linebot.models.messages import ImageMessage


from line回應.models import 圖片表
from line回應.models import 結果影片表


line_bot_api = LineBotApi(settings.YOUR_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(settings.YOUR_CHANNEL_SECRET)


@csrf_exempt
def line介面(request):
    # get X-Line-Signature header value
    signature = request.META['HTTP_X_LINE_SIGNATURE']

    # get request body as text
    body = request.body.decode('utf-8')

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        HttpResponseBadRequest()

    return HttpResponse()


@handler.add(MessageEvent, message=TextMessage)
def 文字(event):
    資料 = event.message.text
    全部圖 = 圖片表.全部圖(event.source)
    影片 = 結果影片表.加影片(全部圖, [], [資料])
    影片網址=影片.影片網址()
    line_bot_api.reply_message(
        event.reply_token,
        [
            TextSendMessage(text=影片網址),
            VideoSendMessage(
                original_content_url='https://www.dropbox.com/s/j69523t6bm9xz3g/Special_Course.mp4?dl=0',
                preview_image_url='https://itaigi.tw/121c4ed080e9127a72d31ae85d1458fc.svg',
            ),
            VideoSendMessage(
                original_content_url=影片網址,
                preview_image_url='https://itaigi.tw/121c4ed080e9127a72d31ae85d1458fc.svg',
            ),
        ]
    )


@handler.add(MessageEvent, message=AudioMessage)
def 聲(event):
    line_bot_api.reply_message(
        event.reply_token,
        [
            TextSendMessage(text='聲', ),
        ]
    )


@handler.add(MessageEvent, message=ImageMessage)
def 圖(event):
    圖片表.加一張圖(
        event.source,
        line_bot_api.get_message_content(event.message.id).iter_content()
    )
    全部圖 = 圖片表.全部圖(event.source)
    line_bot_api.reply_message(
        event.reply_token,
        [
            TextSendMessage(text='這馬有 {} 張背景圖'.format(全部圖.count())),
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
