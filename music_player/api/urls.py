
from django.urls import  path
from .views import MusicRoomView

urlpatterns = [
    path('room', MusicRoomView.as_view())      
]
