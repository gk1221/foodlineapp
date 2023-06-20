from django.db import models
from django.db.models.aggregates import Count

# Create your models here.


class User_Info(models.Model):
    uid = models.CharField(max_length=50, null=False, default='')  # user_id
    name = models.CharField(max_length=255, blank=True, null=False)  # LINE名字
    pic_url = models.CharField(max_length=255, null=False)  # 大頭貼網址
    mtext = models.CharField(max_length=255, blank=True, null=False)  # 文字訊息紀錄
    mdt = models.DateTimeField(auto_now=True)  # 物件儲存的日期時間

    def __str__(self):
        return self.uid


class Location(models.Model):
    area = models.CharField(max_length=20)  # 地區
    name = models.CharField(max_length=100)  # 景點名稱
    address = models.CharField(max_length=500)  # 地址


class foodsheet(models.Model):
    country = models.CharField(max_length=10)  # 縣市
    catagory = models.CharField(max_length=10)  # 種類
    food_1 = models.CharField(max_length=50, default='')
    food_2 = models.CharField(max_length=50)
    food_3 = models.CharField(max_length=50)
    food_4 = models.CharField(max_length=50)
    food_5 = models.CharField(max_length=50)


class StockRecord(models.Model):
    item = models.CharField(max_length=10)
    inout = models.CharField(max_length=5)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    count = models.IntegerField()

    earnper = models.DecimalField(max_digits=3, decimal_places=2, null=True)
    note = models.CharField(max_length=100)
