from django.contrib import admin
from .models import *


class DiaryAdmin(admin.ModelAdmin):
    list_display = ["title", "content", "created_at"]
    fields = (("title", "photo"), "content")

    list_filter = ["title"]  # 過濾器


class TextAdmin(admin.ModelAdmin):
    list_display = ["title", "time_create", "creator", "tag"]
    fields = (("title", "creator"),'tag', "body")
    list_filter = ["tag"]  # 搜尋功能

    def save_model(self, request, obj, form, change):
        if not obj.creator:
            obj.creator = request.user

        obj.save()


admin.site.register(DiaryWrite1, DiaryAdmin)

admin.site.register(Textfarm, TextAdmin)

# admin.site.register(Article)
