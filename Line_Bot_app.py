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
    msg = msg.encode('utf-8')

    reply_msg = '看不懂你說什麼'

    # Add reply 貼圖, do not forget import StickerSendMessage from linebot.model
    if msg == '睡覺':
        sticker_message = StickerSendMessage(
            package_id='1',
            sticker_id='1'
        )
        line_bot_api.reply_message(
            event.reply_token,
            sticker_message)
        return        
    elif msg == '愛妳':
        sticker_message = StickerSendMessage(
            package_id='8525',
            sticker_id='16581301'
        )
        line_bot_api.reply_message(
            event.reply_token,
            sticker_message)
        return        
    elif msg == '好的':
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
    elif msg == '謝謝':
        sticker_message = StickerSendMessage(
            package_id='6362',
            sticker_id='11087928'
        )
        line_bot_api.reply_message(
            event.reply_token,
            sticker_message)
        return        
    elif msg == '加油':
        sticker_message = StickerSendMessage(
            package_id='6362',
            sticker_id='11087933'
        )
        line_bot_api.reply_message(
            event.reply_token,
            sticker_message)
        return        
    elif msg == '好累':
        sticker_message = StickerSendMessage(
            package_id='6362',
            sticker_id='11087923'
        ) 
        line_bot_api.reply_message(
            event.reply_token,
            sticker_message)
        return
    elif msg == '辛苦了':
        sticker_message = StickerSendMessage(
            package_id='8525',
            sticker_id='16581300'
        )
        line_bot_api.reply_message(
            event.reply_token,
            sticker_message)
        return        
    elif msg == '慌張':
        sticker_message = StickerSendMessage(
            package_id='8525',
            sticker_id='16581311'
        )
        line_bot_api.reply_message(
            event.reply_token,
            sticker_message)
        return
    elif msg == '道歉':
        sticker_message = StickerSendMessage(
            package_id='8525',
            sticker_id='16581298'
        )
        line_bot_api.reply_message(
            event.reply_token,
            sticker_message)
        return        
    elif msg == '期待':
        sticker_message = StickerSendMessage(
            package_id='8525',
            sticker_id='16581299'
        )  
        line_bot_api.reply_message(
            event.reply_token,
            sticker_message)
        return        
    elif msg == '問號':
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
    elif msg == '今天天氣好嗎':
        reply_msg = '今天天氣很好, 適合走走'
    elif msg == '早餐想吃什麼':
        reply_msg = '菲力漢堡加蛋跟一杯大冰美式咖啡'
    elif '心情' in msg:
        reply_msg = '每天都要保持好的心情'
    elif msg == '生日快樂':
        # emoji = 
        # [
        #     {
        #         "index": 0, # 要放的位置
        #         "productId": "5ac223c6040ab15980c9b44a", # 所屬組合 ID
        #         "emojiId": "035" # emoji ID
        #     },
        #     {
        #         "index": 37,
        #         "productId": "5ac223c6040ab15980c9b44a",
        #         "emojiId": "008"
        #     }
        # ]
        # line_bot_api.reply_message(
        #     event.reply_token,
        #     TextSendMessage(text='$ 今天是您農曆八月二日誕生日,  祝您生日快樂, 萬事如意, 天天好心情~ $',  emojis=emoji))
        reply_msg = '今天是您農曆八月二日誕生日,  祝您生日快樂, 萬事如意, 天天好心情~'

    line_bot_api.reply_message(
        event.reply_token,
        # 目前修改程式碼的部分, 是調整讓機器人回覆什麼
        #TextSendMessage(text=event.message.text))
        TextSendMessage(text=reply_msg))

if __name__ == "__main__":
    app.run()