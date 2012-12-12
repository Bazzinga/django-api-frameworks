# coding: utf-8
from __future__ import unicode_literals

from django.contrib.auth.models import User, Group
from django.contrib.admin.models import LogEntry
from rest_framework import generics
from .serializers import *


class UserList(generics.ListCreateAPIView):
    model = User
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    model = User
    serializer_class = UserSerializer

class LogEntryList(generics.ListCreateAPIView):
    model = LogEntry
    serializer_class = LogSerializer

class LogEntryDetail(generics.RetrieveUpdateDestroyAPIView):
    model = LogEntry
    serializer_class = LogSerializer
