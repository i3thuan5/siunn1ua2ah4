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
import re


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
    回應 = False
    if event.source.type == 'user':
        回應 = True
        資料 = event.message.text
    elif re.match('[台臺]語[：:]', event.message.text):
        回應 = True
        資料 = event.message.text[3:]
    if 回應:
        全部圖 = 圖片表.全部圖(event.source)
        影片 = 結果影片表.加影片(全部圖, [], [資料])
        line_bot_api.reply_message(
            event.reply_token,
            [
                TextSendMessage(
                    text='完成矣！攏總收著 {} 張背景圖。影片網址： {}'.format(
                        全部圖.count(), 影片.網頁下載網址()
                    )
                ),
                VideoSendMessage(
                    original_content_url=影片.影片網址(),
                    preview_image_url=影片.縮圖網址(),
                ),
            ]
        )
        全部圖.delete()


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
