from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, FollowEvent, UnfollowEvent, StickerSendMessage, ImageSendMessage, LocationSendMessage,
    FlexSendMessage,TemplateSendMessage,ImageCarouselTemplate,ImageCarouselColumn,PostbackAction,PostbackEvent,QuickReplyButton,QuickReply
    ,ConfirmTemplate,MessageAction,ButtonsTemplate
)
# Channel access token
line_bot_api = LineBotApi('GwJntrfFupqCcYDIi44IyJRZdGem64zRHSd1yon+p9LXCy6YV7aq69UNXkKwbtxAkbE+lvdF2fKev8lIq/uACAvm1ObIvtSflNqrCRRXnciMAi6pnlIZ3PlF9IQyszcsnjzrSiId3nNjawTTsJVCTAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('6cd4da9c8fe80dcce6d9403a93e8c9d6')#Channel secret
