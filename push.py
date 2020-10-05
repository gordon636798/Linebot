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

line_bot_api = LineBotApi('CHANNEL_ACCESS_TOKEN')

line_bot_api.push_message('U081d445da00a4d5d75329c291137323c', TextSendMessage(text='Hello World!'))
