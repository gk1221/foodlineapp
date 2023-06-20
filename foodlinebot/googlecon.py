
import pygsheets
import datetime

class google_write():
    def __init__(self, food):
        self.food = food
        self.gc = pygsheets.authorize(service_account_file='client_secret.json')
        self.sht = self.gc.open_by_url(
            'https://docs.google.com/spreadsheets/d/1NwDQFagKUfw8xPI3oxR92LeIjv_11gtcjSXCgLQiTWg/edit?usp=sharing'
        )

    def run(self):
        wks = self.sht.worksheet_by_title('demo')
        s = str(datetime.datetime.now())
        value = [self.food.area, self.food.category, s]
        value = value + self.food.content
        wks.insert_rows(1, values=value)
        print('data inserted')


