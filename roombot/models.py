from django.db import models

from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.


class DiaryWrite1(models.Model):
    title = models.CharField(verbose_name="標題", max_length=100)
    content = models.TextField(verbose_name="內文", blank=True)
    photo = models.ImageField(
        null=True, blank=True, upload_to="photo/", default="photo/rainbow.jpg"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        ans = self.title
        ans += "            -           " + self.content[:5] + "..."
        return ans


class Textfarm(models.Model):

    title = models.CharField(max_length=50, verbose_name="標題")
    body = RichTextUploadingField(verbose_name="內容", default="Type in ..")
    time_create = models.DateTimeField(auto_now_add=True)
    time_edit = models.DateTimeField(auto_now_add=True)
    creator = models.CharField(max_length=20, verbose_name="作者")
    tag = models.CharField(max_length=10, blank=True, verbose_name="標籤", default="Others")

    def __str__(self):
        return self.title

class Testfarm(models.Model):
    time_create = models.DateTimeField(auto_now_add=True)
    body = RichTextUploadingField(verbose_name="內容", default="Type in ..")

    def __str__(self):
        return self.title