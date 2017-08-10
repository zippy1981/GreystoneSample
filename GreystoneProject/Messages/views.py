from __future__ import print_function
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import viewsets

from models import Message
from serializers import MessageSerializer


class Messages(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer