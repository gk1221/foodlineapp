from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import pttdata
from roombot.models import DiaryWrite1, Textfarm


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class PttSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = pttdata
        fields = ['date', 'author', 'title', 'href', 'pushcount', 'content']
        
class DiarySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DiaryWrite1
        fields = ['title', 'content', 'photo', 'created_at']

class TextSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Textfarm
        fields = ['pk','title', 'body', 'time_create', 'time_edit', 'creator', 'tag']