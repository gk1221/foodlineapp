def m1():
    import requests
    import json

    headers = {"Authorization":"Bearer JC4AWZ7AGnx3MQZ5+vo4TIEluPZtK8Nx5crykdbf32GtxHZXKkbCaKhf2IUMnBVRGDl2hCWZYYT4MdjPi8DdC54BoCE6WXWABBfw5P0s468EGaiXCP+d9DZ8QIdjuq5Ky/9wuhbc6nfeAfPBsgdPwwdB04t89/1O/w1cDnyilFU=","Content-Type":"application/json"}

    body = {
        "size": {"width": 1200, "height": 405},
        "selected": "true",
        "name": "Controller",
        "chatBarText": "Controller",
        "areas":[
            {
              "bounds": {"x": 551, "y": 325, "width": 321, "height": 321},
              "action": {"type": "message", "text": "up"}
            },
            {
              "bounds": {"x": 876, "y": 651, "width": 321, "height": 321},
              "action": {"type": "message", "text": "right"}
            },
            {
              "bounds": {"x": 551, "y": 972, "width": 321, "height": 321},
              "action": {"type": "message", "text": "down"}
            },
            {
              "bounds": {"x": 225, "y": 651, "width": 321, "height": 321},
              "action": {"type": "message", "text": "left"}
            },
            {
              "bounds": {"x": 1433, "y": 657, "width": 367, "height": 367},
              "action": {"type": "message", "text": "btn b"}
            },
            {
              "bounds": {"x": 1907, "y": 657, "width": 367, "height": 367},
              "action": {"type": "message", "text": "btn a"}
            }
        ]
      }

    req = requests.request('POST', 'https://api.line.me/v2/bot/richmenu',
                           headers=headers,data=json.dumps(body).encode('utf-8'))

    print(req.text)
def m2():
    from linebot import (
        LineBotApi, WebhookHandler
    )

    line_bot_api = LineBotApi('JC4AWZ7AGnx3MQZ5+vo4TIEluPZtK8Nx5crykdbf32GtxHZXKkbCaKhf2IUMnBVRGDl2hCWZYYT4MdjPi8DdC54BoCE6WXWABBfw5P0s468EGaiXCP+d9DZ8QIdjuq5Ky/9wuhbc6nfeAfPBsgdPwwdB04t89/1O/w1cDnyilFU=')

    with open("image/rich-menu-0.jpg", 'rb') as f:
        line_bot_api.set_rich_menu_image("richmenu-762...", "image/jpeg", f)