from line_bot_api import *
from urllib.parse import parse_qsl
import datetime


#from extensions import db
#from models.user import User
#from models.reservation import Reservation #資料寫入資料庫中
#預約相關功能都會寫在這邊
#增加多個服務項目
services = {
    1:{
        'category':'A餐-雞肉套餐',
        'img_url':'https://i.imgur.com/6Jrc4NX.jpg',
        'title':'打拋雞肉',
        'duration':'熱量:578 大卡',
        'description':'爆香蒜及辣椒，加入碎雞肉拌炒，以小蕃茄及九層塔快拌輔味',
        'price':100,
        'post_url':'https://icook.tw/recipes/66369'
    },
    2:{
        'category':'B餐-豬肉套餐',
        'img_url':'https://i.imgur.com/OO3EM1P.jpg',
        'title':'黑胡椒豬肉',
        'duration':'熱量:786 大卡',
        'description':'醬油醃製豬肉拌炒洋蔥，以黑胡椒粒提香增辣，豐富你味蕾的一刻',
        'price':100,
        'post_url':'https://icook.tw/recipes/66369'
    },
    3:{
        'category':'F餐-蔬菜套餐',
        'img_url':'https://i.imgur.com/zo59nEc.jpg',
        'title':'鍋邊素食',
        'duration':'熱量:354 大卡',
        'description':'燙青菜、低油低鹽調味，清淡的一餐不造成任何負擔',
        'price':80,
        'post_url':'https://icook.tw/recipes/66369'
    },
    4:{
        'category':'G餐-特別套餐',
        'img_url':'https://i.imgur.com/LYZRbcR.jpg',
        'title':'松阪豬肉',
        'duration':'熱量:635 大卡',
        'description':'使用氣炸鍋將肉質自身油脂逼出，原味、天然、就是這樣有嚼勁',
        'price':130,
        'post_url':'https://icook.tw/recipes/66369'
    },

}

def service_category_event(event):
    image_carousel_template_message = TemplateSendMessage(
        alt_text = '請選擇想服務類別',
        template = ImageCarouselTemplate(
            columns = [
                ImageCarouselColumn(
                    image_url='https://i.imgur.com/6Jrc4NX.jpg',
                    action=PostbackAction(
                        lable='A餐-雞肉套餐',
                        dispaly_text='想訂購雞肉套餐',
                        data='action=service&category=A餐-雞肉套餐'
                    )
                ),
                ImageCarouselColumn(
                    image_url='https://i.imgur.com/OO3EM1P.jpg',
                    action=PostbackAction(
                        lable='B餐-豬肉套餐',
                        dispaly_text='想訂購豬肉套餐',
                        data='action=service&category=B餐-豬肉套餐'
                    )
                ),
                ImageCarouselColumn(
                    image_url='https://i.imgur.com/zo59nEc.jpg',
                    action=PostbackAction(
                        lable='F餐-蔬菜套餐',
                        dispaly_text='想訂購蔬菜套餐',
                        data='action=service&category=F餐-蔬菜套餐'
                    )
                ),
                ImageCarouselColumn(
                    image_url='https://i.imgur.com/LYZRbcR.jpg',
                    action=PostbackAction(
                        lable='G餐-特別套餐',
                        dispaly_text='想訂購特別套餐',
                        data='action=service&category=G餐-特別套餐'
                    )
                ),
            ]
        )
    )
    line_bot_api.reply_message(
        event.reply_token,
        [image_carousel_template_message])




def service_event(event):
    #底下三個要等上面的service建立後才寫,主要是要跑service的服務
    #data = dict(parse_qsl(event.postback.data))
    #bubbles = []
    #for service_id in services:
    data = dict(parse_qsl(event.postback.data))

    bubbles = []

    for service_id in services:
        if services[service_id]['category'] == data['category']:
            service = services[service_id]
            bubble = {
              "type": "bubble",
              "hero": {
                "type": "image",
                "size": "full",
                "aspectRatio": "20:13",
                "aspectMode": "cover",
                "url": service['img_url']
              },
              "body": {
                "type": "box",
                "layout": "vertical",
                "spacing": "sm",
                "contents": [
                  {
                    "type": "text",
                    "text": service['title'],
                    "wrap": True,
                    "weight": "bold",
                    "size": "xl"
                  },
                  {
                    "type": "text",
                    "text": service['duration'],
                    "size": "md",
                    "weight": "bold"
                  },
                  {
                    "type": "text",
                    "text": service['description'],
                    "margin": "lg",
                    "wrap": True
                  },
                  {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                      {
                        "type": "text",
                        "text": f"NT$ {service['price']}",
                        "wrap": True,
                        "weight": "bold",
                        "size": "xl",
                        "flex": 0
                      }
                    ],
                    "margin": "xl"
                  }
                ]
              },
              "footer": {
                "type": "box",
                "layout": "vertical",
                "spacing": "sm",
                "contents": [
                  {
                    "type": "button",
                    "style": "primary",
                    "action": {
                      "type": "postback",
                      "label": "預約",
                      "data": f"action=select_date&service_id={service_id}",
                      "displayText": f"我想預約【{service['title']} {service['duration']}】"
                    },
                    "color": "#b28530"
                  },
                  {
                    "type": "button",
                    "action": {
                      "type": "uri",
                      "label": "了解詳情",
                      "uri": service['post_url']
                    }
                  }
                ]
              }
            }

            bubbles.append(bubble)

    flex_message = FlexSendMessage(
        alt_text='請選擇預約項目',
        contents={
          "type": "carousel",
          "contents": bubbles
        }
    )

    line_bot_api.reply_message(
        event.reply_token,
        [flex_message])
#預約日期的功能
#設定完這個function後就要到app.py中的handle_postback去新增判斷式
def service_select_date_event(event):

    data = dict(parse_qsl(event.postback.data))

    weekday_string = {
        0: '一',
        1: '二',
        2: '三',
        3: '四',
        4: '五',
        5: '六',
        6: '日',
    }

    business_day = [1, 2, 3, 4, 5, 6]

    quick_reply_buttons = []

    today = datetime.datetime.today().date()#取得當天的日期
    #weekday()取得星期幾?0是星期一
    for x in range(1, 11):
        day = today + datetime.timedelta(days=x)#透過datetime.timedelta()可以取得隔天的日期

        if day.weekday() in business_day:
            quick_reply_button = QuickReplyButton(
                action=PostbackAction(label=f'{day} ({weekday_string[day.weekday()]})',
                                      text=f'我要預約 {day} ({weekday_string[day.weekday()]}) 這天',
                                      data=f'action=select_time&service_id={data["service_id"]}&date={day}'))
            quick_reply_buttons.append(quick_reply_button)

    text_message = TextSendMessage(text='請問要預約哪一天?',
                                   quick_reply=QuickReply(items=quick_reply_buttons))

    line_bot_api.reply_message(
        event.reply_token,
        [text_message])

#選擇時間的功能
def service_select_time_event(event):

    data = dict(parse_qsl(event.postback.data))

    available_time = ['11:00', '14:00', '17:00', '20:00']

    quick_reply_buttons = []

    for time in available_time:
        quick_reply_button = QuickReplyButton(action=PostbackAction(label=time,
                                                                    text=f'{time} 這個時段',
                                                                    data=f'action=confirm&service_id={data["service_id"]}&date={data["date"]}&time={time}'))
        quick_reply_buttons.append(quick_reply_button)

    text_message = TextSendMessage(text='請問要預約哪個時段?',
                                   quick_reply=QuickReply(items=quick_reply_buttons))
    line_bot_api.reply_message(
        event.reply_token,
        [text_message])


#confirm_template是用來確認,它包含了訊息和底下有兩個按鈕
#PostbackAction可以帶data的資料,MessageAction則是用戶按下去時會直接傳訊息到聊天室
def service_confirm_event(event):

    data = dict(parse_qsl(event.postback.data))
    booking_service = services[int(data['service_id'])]#取得要預約的服務項目資料,會出現1234對應到上面的service

    confirm_template_message = TemplateSendMessage(
        alt_text='請確認預約項目',
        template=ConfirmTemplate(
            text=f'您即將預約\n\n{booking_service["title"]} {booking_service["duration"]}\n預約時段: {data["date"]} {data["time"]}\n\n確認沒問題請按【確定】',
            actions=[
                PostbackAction(
                    label='確定',
                    display_text='確認沒問題!',
                    data=f'action=confirmed&service_id={data["service_id"]}&date={data["date"]}&time={data["time"]}'
                ),
                MessageAction(
                    label='重新預約',
                    text='我想重新預約'
                )
            ]
        )
    )
    line_bot_api.reply_message(
        event.reply_token,
        [confirm_template_message])

#取消用的是ButtonsTemplat,有訊息的標題和訊息的內容
#action中可以設定一到四個按鈕
#這個function是判斷用戶是否預約過,利用Reservation.query.filter搜尋資料,條件是user_id == user.id


