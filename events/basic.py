from line_bot_api import *


def about_us_event(event):
    emoji = [
        {
            "index": 0,
            "productId": "5ac2211e031a6752fb806d61",
            "emojiId": "189"
        },
        {
            "index": 9,
            "productId": "5ac2211e031a6752fb806d61",
            "emojiId": "085"
        }
    ]

    text_message = TextSendMessage(text='''$ 始午健康餐盒 $
原型食物-提供您每日健康的一餐

營養標示-計算健康的每一步

拒絕精緻-紫米、糙米、紅藜

保溫用膳-提供保溫裝備直到您用餐

  (每日供膳菜單如下圖)。''', emojis=emoji)

    sticker_message = StickerSendMessage(
        package_id='6362',
        sticker_id='11087932'
    )

    about_us_img = 'https://i.imgur.com/w9FlofV.jpg'

    image_message = ImageSendMessage(
        original_content_url=about_us_img,
        preview_image_url=about_us_img
    )

    line_bot_api.reply_message(
        event.reply_token,
        [text_message, sticker_message, image_message])
    
def location_event(event):
    location_message = LocationSendMessage(
        title='始午',
        address='802高雄市苓雅區仁德街56號之1號',
        latitude=22.6161720233321,
        longitude=120.30221104716944
    )

    line_bot_api.reply_message(
        event.reply_token,
        location_message)