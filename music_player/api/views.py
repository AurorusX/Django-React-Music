from django.shortcuts import render
from rest_framework import generics
from .serializers import MusicRoomSerializer
from .models import MusicRoom

# Create your views here.

class MusicRoomView(generics.ListAPIView):
    queryset=MusicRoom.objects.all()
    serializer_class=MusicRoomSerializer
