# 1. 用 flask 架設伺服器
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, StickerSendMessage, TemplateSendMessage
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

    # Add reply 貼圖, do not forget import StickerSendMessage from linebot.model
    if msg == '睡覺貼圖':
        sticker_message = StickerSendMessage(
            package_id='1',
            sticker_id='1'
        )
        line_bot_api.reply_message(
        event.reply_token,
        sticker_message)
        return        
    elif msg == '愛妳貼圖':
        sticker_message = StickerSendMessage(
            package_id='8525',
            sticker_id='16581301'
        )
        line_bot_api.reply_message(
        event.reply_token,
        sticker_message)
        return        
    elif msg == '好的貼圖':
        sticker_message = StickerSendMessage(
            package_id='6370',
            sticker_id='11088016'
        )
        line_bot_api.reply_message(
        event.reply_token,
        sticker_message)
        return        
    elif msg == '休息貼圖':
        sticker_message = StickerSendMessage(
            package_id='6362',
            sticker_id='11087930'
        )  
        line_bot_api.reply_message(
        event.reply_token,
        sticker_message)
        return        
    elif msg == '謝謝貼圖':
        sticker_message = StickerSendMessage(
            package_id='6362',
            sticker_id='11087928'
        )
        line_bot_api.reply_message(
        event.reply_token,
        sticker_message)
        return        
    elif msg == '加油貼圖':
        sticker_message = StickerSendMessage(
            package_id='6362',
            sticker_id='11087933'
        )
        line_bot_api.reply_message(
        event.reply_token,
        sticker_message)
        return        
    elif msg == '好累貼圖':
        sticker_message = StickerSendMessage(
            package_id='6362',
            sticker_id='11087923'
        ) 
        line_bot_api.reply_message(
        event.reply_token,
        sticker_message)
        return
    elif msg == '辛苦貼圖':
        sticker_message = StickerSendMessage(
            package_id='8525',
            sticker_id='16581300'
        )
        line_bot_api.reply_message(
        event.reply_token,
        sticker_message)
        return        
    elif msg == '慌張貼圖':
        sticker_message = StickerSendMessage(
            package_id='8525',
            sticker_id='16581311'
        )
        line_bot_api.reply_message(
        event.reply_token,
        sticker_message)
        return
    elif msg == '道歉貼圖':
        sticker_message = StickerSendMessage(
            package_id='8525',
            sticker_id='16581298'
        )
        line_bot_api.reply_message(
        event.reply_token,
        sticker_message)
        return        
    elif msg == '期待貼圖':
        sticker_message = StickerSendMessage(
            package_id='8525',
            sticker_id='16581299'
        )  
        line_bot_api.reply_message(
        event.reply_token,
        sticker_message)
        return        
    elif msg == '問號貼圖':
        sticker_message = StickerSendMessage(
            package_id='8525',
            sticker_id='16581306'
        )
        line_bot_api.reply_message(
        event.reply_token,
        sticker_message)
        return

    if msg == '選擇餐廳':
        buttons_template_message = TemplateSendMessage(
            alt_text='Buttons template',
            template=ButtonsTemplate(
            title='Restaurant Menu',
            text='請選擇類型',
                actions=[
                    MessageTemplateAction(
                        label='台式餐廳',
                        text='option one',
                     ),
                    MessageTemplateAction(
                        label='義式餐廳',
                        text='option two',
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, buttons_template_message)
        return

    if msg in ['hi', 'Hi']:
        reply_msg = 'hi, how are you ?'
    elif msg == '你吃飯了嗎':
        reply_msg = '還沒'
    elif msg == '你是誰':
        reply_msg = '我是機器人'
    elif '訂位' in msg:
        reply_msg = '您想訂位, 是嗎?'
    elif msg == '今天天氣好嗎':
        reply_msg = '今天天氣很好, 適合走走'
    elif msg == '早餐想吃什麼':
        reply_msg = '菲力漢堡加蛋跟一杯大冰美式咖啡'
    elif '心情' in msg:
        reply_msg = '每天都要保持好的心情'
    elif '情人節快樂' in msg:
        reply_msg = 'Dear Peggy 2022 情人節快樂, 很開心, 很幸運能有您這位那麼棒的女友, 喜歡跟您再一起的任何時光, 雖然不像其他人常到處玩或是大魚大肉, 但是我更喜歡跟您充滿愛的相處時光XD'

    line_bot_api.reply_message(
        event.reply_token,
        # 目前修改程式碼的部分, 是調整讓機器人回覆什麼
        #TextSendMessage(text=event.message.text))
        TextSendMessage(text=reply_msg))

if __name__ == "__main__":
    app.run()