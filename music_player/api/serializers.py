from rest_framework import serializers
from .models import MusicRoom


class MusicRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model= MusicRoom
        fields=('id','code', 'host','can_pause',
                'votes_to_skip','created_at')