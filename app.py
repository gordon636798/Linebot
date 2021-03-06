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

import re
import requests
import json

app = Flask(__name__)

line_bot_api = LineBotApi('CHANNEL_ACCESS_TOKEN')
handler = WebhookHandler('CHANNEL_SECRET')

users = {}



@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    #print(body)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    id = event.source.user_id
    print(id)
    profile = line_bot_api.get_profile(id)
    print(profile)
    if event.message.text =='你老師':
        message = TextSendMessage(text='許政穆老師')
        line_bot_api.reply_message(event.reply_token, message)

    elif event.message.text =='學校':
        url = request.url_root +'static/tmp/test/' + 'test.png'
        url = url.replace('http','https')
        #print(url)
        message = ImageSendMessage(url,url)
        line_bot_api.reply_message(event.reply_token, message)
    
    elif event.message.text == '學校資訊':
        f = json.load(open('./test.json'))
        print(f)
        flex_message = FlexSendMessage(
        alt_text='hello',
            contents=f
        )
        line_bot_api.reply_message(event.reply_token, flex_message)
    elif event.message.text == '公告':
        import spider
        tags = spider.tags
        
        messages = []
        for tag in tags:
            messages.append(TextSendMessage(text=tag.text))
        line_bot_api.reply_message(event.reply_token, messages)
        
    
    



if __name__ == "__main__":
    app.run()

