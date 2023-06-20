import beautifulsoup4
import requests

url = "https://lol.moa.tw/summoner/show/"
LolID = "我愛英雄聯盟958"
html = requests.get(url+LolID)
print(html)

try:
    