from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
line_bot_api = LineBotApi(os.getenv("LINE_CHANNEL_ACCESS_TOKEN"))
handler = WebhookHandler(os.getenv("LINE_CHANNEL_SECRET"))

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    area = event.message.text.strip()
    url = 'https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json'
    try:
        datas = requests.get(url).json()
        result = ''
        for d in datas:
            if d['sarea'] == area:
                result += f"{d['sna'][11:]}：{d['available_return_bikes']} 空位\n"
        if result == '':
            result = '查無資料，請輸入正確行政區（如：大安、中山）'
    except:
        result = '資料取得失敗，請稍後再試。'

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=result)
    )

if __name__ == "__main__":
    app.run()
