from django.contrib.auth.models import User, Group
from rest_framework.permissions import AllowAny
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer, GroupSerializer, PttSerializer, DiarySerializer, TextSerializer
from .models import pttdata
from roombot.models import DiaryWrite1, Textfarm

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class PttViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = pttdata.objects.all()
    serializer_class = PttSerializer
    permission_classes = [permissions.IsAuthenticated]


class DiaryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = DiaryWrite1.objects.all()
    serializer_class = DiarySerializer
    permission_classes = []

class TextViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Textfarm.objects.all()
    serializer_class = TextSerializer
    permission_classes = []

