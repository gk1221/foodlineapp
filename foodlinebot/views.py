from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import (
    MessageEvent,
    TextSendMessage,
    TemplateSendMessage,
    ButtonsTemplate,
    LocationSendMessage,
    MessageTemplateAction,
    PostbackEvent,
    PostbackTemplateAction,
    ConfirmTemplate,
    CarouselTemplate,
    CarouselColumn,
    URITemplateAction,
)
from .scraper1 import IFoodie
from .models import Location
from .actdata import actdata
from .menu import StockEarn

# from .googlecon import google_write

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)


@csrf_exempt
def callback(request):
    if request.method == "POST":
        signature = request.META["HTTP_X_LINE_SIGNATURE"]
        body = request.body.decode("utf-8")

        try:
            events = parser.parse(body, signature)  # 傳入的事件
            # print('\ninput events:\n')
            # print(events)
        except InvalidSignatureError:
            print("---------------------------error 1")
            return HttpResponseForbidden()
        except LineBotApiError:
            print("--------------------------error 2")
            return HttpResponseBadRequest()
        is_post = False
        for event in events:

            if isinstance(event, MessageEvent):  # 如果有訊息事件
                print("\ninput text:  " + event.message.text)
                if event.message.text == "哈囉":
                    line_bot_api.reply_message(  # 01回應前五間最高人氣且營業中的餐廳訊息文字
                        event.reply_token,
                        TemplateSendMessage(
                            alt_text="選擇地區",
                            template=ButtonsTemplate(
                                title="縣市選單",
                                text="點選地區或輸入縣市",
                                actions=[
                                    PostbackTemplateAction(
                                        label="台北市", text="台北市", data="A:台北市"
                                    ),
                                    PostbackTemplateAction(
                                        label="台中市", text="台中市", data="A:台中市"
                                    ),
                                    PostbackTemplateAction(
                                        label="高雄市", text="高雄市", data="A:高雄市"
                                    ),
                                ],
                            ),
                        ),
                    )

                elif "股票" in event.message.text:

                    if "查詢" in event.message.text:
                        # 股票 查詢 台積電
                        print("you got this")
                        tex = event.message.text.split()

                        s1 = actdata()
                        print(tex)
                        ans = s1.stock_select()
                        print(type(ans[0][3]))

                        ans2 = []
                        for i in ans:
                            x1 = []
                            for j in range(len(i)):
                                if (j == 4 or j == 6) and i[j] != None:
                                    x1.append(float(i[j]))
                                else:
                                    x1.append(i[j])
                            print(x1)
                            ans2.append(x1)
                            print(x1)
                            ans2.append(list(i))

                        print(ans2)

                        print(type(ans2))
                        print(type(ans2[0]))
                        line_bot_api.reply_message(
                            event.reply_token, TextSendMessage(
                                text=ans2)
                        )

                    elif "新增" in event.message.text:
                        # 股票 新增 台積電 買 600 50
                        # 股票 新增 台積電 賣 601 50 無 2.3
                        tex = event.message.text.split()
                        stock_list = []
                        for i in range(6):
                            try:
                                stock_list.append(tex[2+i])
                            except:
                                stock_list.append("")

                        print(stock_list)
                        s1 = actdata()
                        ans = s1.stock(stock_list)
                        print(ans)

                        line_bot_api.reply_message(
                            event.reply_token, TextSendMessage(text="updating")
                        )

                elif event.message.text == "Carousel template":
                    Carousel_template = TemplateSendMessage(
                        alt_text="Carousel template",
                        template=CarouselTemplate(
                            columns=[
                                CarouselColumn(
                                    thumbnail_image_url="https://lh3.googleusercontent.com/QCExcuh6FbCXh6AtQeWrwxC99ukwJYgpkwM4I99snXj6s9UoIlUqFw9h8LTiDqpNMZfJUTYWFoVWuSSP53snqNpPsXUKcghg=s360",
                                    title="this is menu1",
                                    text="description1",
                                    actions=[
                                        PostbackTemplateAction(
                                            label="postback1",
                                            text="postback text1",
                                            data="action=buy&itemid=1",
                                        ),
                                        MessageTemplateAction(
                                            label="message1", text="message text1"
                                        ),
                                        URITemplateAction(
                                            label="uri1",
                                            uri="https://www.youtube.com/watch?v=srks-fOx-O4",
                                        ),
                                    ],
                                ),
                                CarouselColumn(
                                    thumbnail_image_url="https://lh3.googleusercontent.com/Z4vYba2SOHt07TbdRr5zz3_lUDRB9-ZjyEoih3CQEvJCuQ0wKj7-DfcEK58XhqD3tusVnu8gzxvOMNM2oxDIx5BB3Z9HE3Xx=s360",
                                    title="this is menu2",
                                    text="description2",
                                    actions=[
                                        PostbackTemplateAction(
                                            label="postback2",
                                            text="postback text2",
                                            data="action=buy&itemid=2",
                                        ),
                                        MessageTemplateAction(
                                            label="message2", text="message text2"
                                        ),
                                        URITemplateAction(
                                            label="連結2", uri="http://example.com/2"
                                        ),
                                    ],
                                ),
                            ]
                        ),
                    )
                    line_bot_api.reply_message(
                        event.reply_token, Carousel_template)

                elif event.message.text == "位置":
                    line_bot_api.reply_message(
                        event.reply_token,
                        LocationSendMessage(
                            title="my location",
                            address="Tainan",
                            latitude=22.994821,
                            longitude=120.196452,
                        ),
                    )

                elif event.message.text == "說明":
                    line_bot_api.reply_message(  # 01回應前五間最高人氣且營業中的餐廳訊息文字
                        event.reply_token,
                        TextSendMessage(
                            text="點選開始\n或輸入 「地區 美食」 \n例如「台北市 早餐」\n\n\n "
                            "~使用資料庫~\n使用「資料庫查詢」\n或用:\n「資料庫新增\n  高雄市 火鍋」"
                        ),
                    )

                elif "資料庫" in event.message.text:

                    if "查詢" in event.message.text:
                        print("GO !")
                        try:
                            print("GO  ")
                            s1 = actdata()
                            textac = s1.select()
                            print(textac)
                            print(textac[0])
                            print(type(textac))

                            line_bot_api.reply_message(
                                event.reply_token, TextSendMessage(text="成功")
                            )
                            line_bot_api.reply_message(
                                event.reply_token, TextSendMessage(
                                    text=str(textac[0]))
                            )

                        except LineBotApiError:
                            print("ERR 1 ")

                            line_bot_api.reply_message(
                                event.reply_token,
                                TextSendMessage(text="失敗"),
                            )
                        except InvalidSignatureError:
                            print("ERR 2")
                            line_bot_api.reply_message(
                                event.reply_token,
                                TextSendMessage(text=HttpResponseForbidden()),
                            )

                    elif "新增" in event.message.text:
                        tex = event.message.text.split("\n")
                        tex = tex[1].split(" ")
                        tex = [str(i) for i in tex]
                        s1 = actdata()
                        print(tex)

                        ans = s1.insert(tex)
                        print(ans)

                        line_bot_api.reply_message(
                            event.reply_token, TextSendMessage(text="updating")
                        )
                    else:
                        line_bot_api.reply_message(
                            event.reply_token, TextSendMessage(text="資料不完全")
                        )

                else:
                    str_list = event.message.text.split(" ")

                    if len(str_list) == 2:
                        food = IFoodie(str_list[0], str_list[1])  # 地區  # 美食類別
                        txt = f"   《{str_list[0]} {str_list[1]}》\n{food.scrape()}"
                        # ga = google_write(food)
                        # ga.run()

                        line_bot_api.reply_message(  # 回復訊息文字
                            event.reply_token,
                            # 爬取該地區正在營業，且符合所選擇的美食類別的前五大最高人氣餐廳
                            TextSendMessage(text=txt),
                        )

                    elif len(str_list) == 3:

                        locations = Location.objects.filter(area=str_list[1])

                        content = ""  # 回覆使用者的內容
                        for location in locations:
                            content += location.name + "\n" + location.address + "\n\n"

                        line_bot_api.reply_message(  # 回覆訊息
                            event.reply_token, TextSendMessage(text=content)
                        )

                    else:
                        if not is_post:
                            line_bot_api.reply_message(  # 回復訊息文字
                                event.reply_token,
                                # 爬取該地區正在營業，且符合所選擇的美食類別的前五大最高人氣餐廳
                                TextSendMessage(
                                    text="格式錯誤\n請點選開始 或輸入 「地區 美食」 \n例如「台北市 早餐」"
                                ),
                            )
            if isinstance(event, PostbackEvent):  # 如果有回傳值事件
                is_post = True
                print("----------" + event.postback.data[:])
                if event.postback.data[0:1] == "A":  # 如果回傳值為「選擇地區」

                    area = event.postback.data[2:]  # 透過切割字串取得地區文字

                    line_bot_api.reply_message(  # 回復「選擇美食類別」按鈕樣板訊息
                        event.reply_token,
                        TemplateSendMessage(
                            alt_text="Buttons template",
                            template=ButtonsTemplate(
                                title="類別選單",
                                text="請選擇美食類別",
                                actions=[
                                    PostbackTemplateAction(  # 將第一步驟選擇的地區，包含在第二步驟的資料中
                                        label="火鍋", text="火鍋", data="B:" + area + ":火鍋"
                                    ),
                                    PostbackTemplateAction(
                                        label="早午餐",
                                        text="早午餐",
                                        data="B:" + area + ":早午餐",
                                    ),
                                    PostbackTemplateAction(
                                        label="約會餐廳",
                                        text="約會餐廳",
                                        data="B:" + area + ":約會餐廳",
                                    ),
                                ],
                            ),
                        ),
                    )

                elif event.postback.data[0:1] == "B":  # 如果回傳值為「選擇美食類別」

                    result = event.postback.data[2:]  # 回傳值的字串切割

                    Confirm_template = TemplateSendMessage(
                        alt_text="需要食記?",
                        template=ConfirmTemplate(
                            title="需要食記?",
                            text="選擇是否需要食記",
                            actions=[
                                PostbackTemplateAction(
                                    label="是", text="Y", data="C:Y:" + result
                                ),
                                PostbackTemplateAction(
                                    label="否", text="N", data="C:N:" + result
                                ),
                            ],
                        ),
                    )
                    line_bot_api.reply_message(
                        event.reply_token, Confirm_template)

                elif event.postback.data[0:1] == "C":

                    result = event.postback.data[2:].split(":")

                    food = IFoodie(result[1], result[2],
                                   result[0])  # 地區  # 美食類別

                    line_bot_api.reply_message(  # 回復訊息文字
                        event.reply_token,
                        # 爬取該地區正在營業，且符合所選擇的美食類別的前五大最高人氣餐廳
                        TextSendMessage(text=food.scrape(), emojis="\U0001F449Unicode emoji\U0001F448"),
                    )

        return HttpResponse("Bad Request")
    else:
        print("------------------------------------fail")
        return HttpResponseBadRequest()


"""
                else:
                    print('========================')
                    food = IFoodie(event.message.text)

                    r = food.scrape()

                    if r != '':
                        line_bot_api.reply_message(  # 02回應前五間最高人氣且營業中的餐廳訊息文字
                            event.reply_token,
                            TextSendMessage(text=food.scrape())
                        )
                    else:
                        line_bot_api.reply_message(  # 02回應前五間最高人氣且營業中的餐廳訊息文字
                            event.reply_token,
                            TextSendMessage(text='錯誤\n請重新輸入縣市\n或輸入哈囉開啟選單')
                        )
        print('!!!!!done')
"""
