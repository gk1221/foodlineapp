import json
from abc import ABC, abstractmethod

import requests
from bs4 import BeautifulSoup

# import datetime


class Food(ABC):
    def __init__(self, area="高雄市", category="火鍋", comment="N"):
        self.area = area  # 地區
        self.category = category  # 美食類別
        self.comment = comment
        self.content = []

    @abstractmethod
    def scrape(self):
        pass


class IFoodie(Food):
    def scrape(self):
        url = (
            "https://ifoodie.tw/explore/"
            + self.area
            + "/list/"
            + self.category
            + "?sortby=popular"
        )

        response = requests.get(url)

        soup = BeautifulSoup(response.content, "html.parser")

        """舊法
        cards = soup.find_all(
            "div",
            {
                "class": "jsx-3757653001 restaurant-item track-impression-ga",
                "class": "jsx-3757653001 restaurant-item track-impression-ga takeout",
                "class": "jsx-3757653001 restaurant-item  track-impression-ga active",
            },
            limit=15,
        )
        print("-------------------{:15}-------------------".format("Making Reply"))
        for card in cards:
            title = card.find(  # 餐廳名稱
                "a", {"class": "jsx-3757653001 title-text"}
            ).getText()
            self.content.append(title)
            stars = card.find("div", {"class": "jsx-1207467136 text"}).getText()  # 餐廳評價

            address = card.find(  # 餐廳地址
                "div", {"class": "jsx-3757653001 address-row"}
            ).getText()
            webb = ""
            if self.comment == "Y":
                webb = self.get_comment(title)

            # 將取得的餐廳名稱、評價及地址連結一起，並且指派給content變數
            content += f"{title} \n{stars}顆星 \n{address} \n{webb}\n"
            print(content)
        print("-------------------{:15}-------------------".format("Reply Success"))
        """

        # catch json

        jsoncard = soup.find("script", {"id": "__NEXT_DATA__"}).contents
        str_card = str(jsoncard[0])
        j1 = json.loads(str_card)
        res = j1["props"]["initialState"]["search"]["explore"]["data"]
        ans = ""
        # processing
        for ar in res:
            title = ar["name"]
            rate = ar["rating"]
            addr = ar["address"]
            comme = ""
            self.content.append([title, rate, addr])
            if self.comment=="Y":
                comme = self.get_comment(title)
            ans += f"{title} \n{rate}顆星 \n{addr}\n{comme}\n"
        return ans

    def get_comment(self, restur):
        URL = f"https://www.google.com.tw/search?q=食記 {restur}"
        USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"

        headers = {"user-agent": USER_AGENT}
        resp = requests.get(URL, headers=headers)
        soup = BeautifulSoup(resp.content, "html.parser")

        a = soup.find("div", {"class": "g"}, "a")
        link = a.a["href"]
        return link

    def run(self):
        wks = self.sht.worksheet_by_title("demo")
        s = str(datetime.datetime.now())
        print(s)
        value = [self.food.area, self.food.category, s]
        value = value + self.food.content
        print(value)
        wks.insert_rows(1, values=value)

    def select(self):
        wks = self.sht.worksheet_by_title("demo")
        df2 = wks.get_as_df(
            has_header=True,
            start="A1",
            index_colum=1,
            empty_value="",
            include_tailing_empty=True,
        )  # index 從 1 開始算
        return df2



