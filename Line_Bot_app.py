# 1. 用 flask 架設伺服器
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
# from linebot.models import (
#     MessageEvent, TextMessage, TextSendMessage, StickerSendMessage, TemplateSendMessage
# )
from linebot.models import *
import re

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
    #msg = msg.encode('utf-8')

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
                        ),
                        URITemplateAction(
                            label='Happy Bithday Song',
                            uri='https://drive.google.com/file/d/16tp9lgHW2EiIu1wYtgTH4GEQHwa3CYk3/view?usp=sharing'
                        )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, buttons_template_message)
        return

    if msg == '生日快樂歌':
        buttons_template_message = TemplateSendMessage(
            alt_text='Happy Birthday',
            template=ButtonsTemplate(
                title='Happy Birthday Song',
                text='Happy Birthday to Peggy',
                actions=[
                        URIAction(
                            label='Happy Birthday Song',
                            uri='https://drive.google.com/file/d/16tp9lgHW2EiIu1wYtgTH4GEQHwa3CYk3/view?usp=sharing'
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
    elif msg == '祝福Peggy生日快樂':
        flex_message = FlexSendMessage(
            alt_text='Happy Birthdar',
            contents={
  "type": "bubble",
  "hero": {
    "type": "image",
    "url": "https://i.imgur.com/fOa2zJx.jpg",
    "size": "full",
    "aspectRatio": "20:13",
    "aspectMode": "cover",
    "action": {
      "type": "uri",
      "uri": "https://linecorp.com"
    }
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "spacing": "md",
    "action": {
      "type": "uri",
      "uri": "https://linecorp.com"
    },
    "contents": [
      {
        "type": "text",
        "text": "Peggy's Birthday 2022",
        "size": "xl",
        "weight": "bold"
      },
      {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
          {
            "type": "box",
            "layout": "baseline",
            "contents": [
              {
                "type": "icon",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/restaurant_regular_32.png"
              },
              {
                "type": "text",
                "text": "衣服",
                "weight": "bold",
                "margin": "sm",
                "flex": 0,
                "action": {
                  "type": "uri",
                  "label": "action",
                  "uri": "https://ec.elifemall.com.tw/products/2096605"
                }
              },
              {
                "type": "text",
                "text": "相關物品",
                "size": "sm",
                "align": "end",
                "color": "#aaaaaa"
              }
            ]
          },
          {
            "type": "box",
            "layout": "baseline",
            "contents": [
              {
                "type": "icon",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/restaurant_large_32.png"
              },
              {
                "type": "text",
                "text": "背",
                "weight": "bold",
                "margin": "sm",
                "flex": 0,
                "action": {
                  "type": "uri",
                  "label": "action",
                  "uri": "https://www.doughnut.com.tw/SalePage/Index/7714223"
                }
              },
              {
                "type": "text",
                "text": "生財工具",
                "size": "sm",
                "align": "end",
                "color": "#aaaaaa"
              }
            ]
          },
          {
            "type": "box",
            "layout": "baseline",
            "contents": [
              {
                "type": "icon",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/restaurant_regular_32.png"
              },
              {
                "type": "text",
                "text": "耳朵",
                "weight": "bold",
                "margin": "sm",
                "flex": 0,
                "action": {
                  "type": "uri",
                  "label": "action",
                  "uri": "https://www.apple.com/tw/airpods-3rd-generation/"
                }
              },
              {
                "type": "text",
                "text": "放鬆器具",
                "size": "sm",
                "align": "end",
                "color": "#aaaaaa"
              }
            ]
          },
          {
            "type": "box",
            "layout": "baseline",
            "contents": [
              {
                "type": "icon",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/restaurant_large_32.png"
              },
              {
                "type": "text",
                "text": "眼睛",
                "weight": "bold",
                "margin": "sm",
                "flex": 0,
                "action": {
                  "type": "uri",
                  "label": "action",
                  "uri": "https://www.owndays.com/tw/zh_tw"
                }
              },
              {
                "type": "text",
                "text": "靈魂之窗",
                "size": "sm",
                "align": "end",
                "color": "#aaaaaa"
              }
            ]
          },
          {
            "type": "box",
            "layout": "baseline",
            "contents": [
              {
                "type": "icon",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/restaurant_regular_32.png"
              },
              {
                "type": "text",
                "text": "其他",
                "weight": "bold",
                "margin": "sm",
                "flex": 0,
                "action": {
                  "type": "uri",
                  "label": "action",
                  "uri": "https://i.imgur.com/e7GERSM.jpg"
                }
              },
              {
                "type": "text",
                "text": "萬能利器",
                "size": "sm",
                "align": "end",
                "color": "#aaaaaa"
              }
            ]
          }
        ]
      },
      {
        "type": "text",
        "wrap": True,
        "color": "#aaaaaa",
        "size": "xxs",
        "text": "Choose an option that you like, maybe I can help you realize"
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "button",
        "style": "primary",
        "color": "#905c44",
        "margin": "xxl",
        "action": {
          "type": "uri",
          "label": "Decision",
          "uri": "https://i.imgur.com/8uM02O7.jpg"
        }
      }
    ]
  }
}
        )
        line_bot_api.reply_message(event.reply_token, flex_message)
        # line_bot_api.reply_message(
        #     event.reply_token,
        #     TextSendMessage(text="$ 今天是您農曆八月二日誕生日,  祝您生日快樂, 萬事如意, 天天好心情~ $",  emojis=emoji)
        # )
        #reply_msg = '今天是您農曆八月二日誕生日,  祝您生日快樂, 萬事如意, 天天好心情~'
        return

    line_bot_api.reply_message(
        event.reply_token,
        # 目前修改程式碼的部分, 是調整讓機器人回覆什麼
        #TextSendMessage(text=event.message.text))
        TextSendMessage(text=reply_msg))

if __name__ == "__main__":
    app.run()