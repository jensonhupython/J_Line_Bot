# 1. 用 flask 架設伺服器
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('Q+ACqQXK7JI1MGp8J4K2jKoj71irtyhxO9W4vR/vrdY9NewL4/0Z353Yi427gPUNXFX9i+mBSU6AgOqP72I5yO2heylmFmlVAzKf4aSvZ9Gjmx9lzsHV+yXg9i4pRRBZRlraG/dTgeGwjbMoFxgfPwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('7f6587e82ce905e441ff65fe981299a2')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
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
    msg = event.message.text
    reply_msg = '看不懂你說什麼'

    if msg in ['hi', 'Hi']:
        reply_msg = 'hi, how are you ?'
    elif msg == '你吃飯了嗎':
        reply_msg = '還沒'
    elif msg == '你是誰':
        reply_msg = '我是機器人'
    elif '訂位' in msg:
        reply_msg = '您想訂位, 是嗎?'

    line_bot_api.reply_message(
        event.reply_token,
        # 目前修改程式碼的部分, 是調整讓機器人回覆什麼
        #TextSendMessage(text=event.message.text))
        TextSendMessage(text=reply_msg))

if __name__ == "__main__":
    app.run()