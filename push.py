from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)

from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, ImageSendMessage, FlexSendMessage
)

line_bot_api = LineBotApi('66QuFSr22occhn5pWWZgiNHPlNiAkOmbPltgdKEwodeRi3ipqJhTnj4l4TILfrtgXcz1mrxOJjfnPBPeLgqZvrMm0UFJzo9wBahXTUFRhwTseht5pJg/3KVGkqL9uGSrKGdR669woiNKYg7Az01aawdB04t89/1O/w1cDnyilFU=')

line_bot_api.push_message('U081d445da00a4d5d75329c291137323c', TextSendMessage(text='Hello World!'))